import os
import sys
import boto3
import pandas as pd
from src.configuration.aws_connection import get_minio_client
from src.constants import *
from src.exception import MyException
from src.logger import logging


class MinIOStorage:
    """
    Class for handling MinIO storage operations as an alternative to AWS S3
    Provides methods for uploading, downloading, and managing model artifacts
    """
    
    def __init__(self):
        self.client = get_minio_client()
        self.bucket_name = MODEL_BUCKET_NAME
    
    def create_bucket(self):
        """
        Creates a bucket in MinIO if it doesn't exist
        """
        try:
            # Check if bucket exists
            response = self.client.list_buckets()
            bucket_names = [bucket['Name'] for bucket in response['Buckets']]
            
            if self.bucket_name not in bucket_names:
                logging.info(f"Creating bucket: {self.bucket_name}")
                self.client.create_bucket(Bucket=self.bucket_name)
                logging.info(f"Bucket {self.bucket_name} created successfully")
            else:
                logging.info(f"Bucket {self.bucket_name} already exists")
                
        except Exception as e:
            raise MyException(e, sys) from e
    
    def upload_file(self, local_file_path: str, s3_key: str):
        """
        Uploads a file to MinIO bucket
        :param local_file_path: Path to local file to upload
        :param s3_key: Key (path) to store the file in MinIO
        """
        try:
            logging.info(f"Uploading file {local_file_path} to MinIO bucket {self.bucket_name} with key {s3_key}")
            
            # Ensure bucket exists
            self.create_bucket()
            
            # Upload file
            self.client.upload_file(local_file_path, self.bucket_name, s3_key)
            logging.info(f"File uploaded successfully to {s3_key}")
            
        except Exception as e:
            raise MyException(e, sys) from e
    
    def download_file(self, s3_key: str, local_file_path: str):
        """
        Downloads a file from MinIO bucket
        :param s3_key: Key (path) of the file in MinIO
        :param local_file_path: Local path to save the downloaded file
        """
        try:
            logging.info(f"Downloading file {s3_key} from MinIO bucket {self.bucket_name} to {local_file_path}")
            
            # Download file
            self.client.download_file(self.bucket_name, s3_key, local_file_path)
            logging.info(f"File downloaded successfully to {local_file_path}")
            
        except Exception as e:
            raise MyException(e, sys) from e
    
    def list_files(self, prefix: str = ""):
        """
        Lists files in the MinIO bucket with optional prefix
        :param prefix: Optional prefix to filter files
        :return: List of file keys
        """
        try:
            response = self.client.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
            files = [obj['Key'] for obj in response.get('Contents', [])]
            return files
        except Exception as e:
            raise MyException(e, sys) from e
    
    def delete_file(self, s3_key: str):
        """
        Deletes a file from MinIO bucket
        :param s3_key: Key (path) of the file to delete
        """
        try:
            logging.info(f"Deleting file {s3_key} from MinIO bucket {self.bucket_name}")
            self.client.delete_object(Bucket=self.bucket_name, Key=s3_key)
            logging.info(f"File {s3_key} deleted successfully")
        except Exception as e:
            raise MyException(e, sys) from e


# For backward compatibility, we'll also provide a class with the original name
class AWSS3Storage(MinIOStorage):
    pass