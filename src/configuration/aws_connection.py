import boto3
import os
from src.constants import *

def get_minio_client():
    """
    Creates and returns a MinIO client using boto3 (S3 compatible API)
    MinIO is used as an alternative to AWS S3 for local model storage
    """
    try:
        # Create a boto3 client configured for MinIO
        minio_client = boto3.client(
            's3',
            endpoint_url=MINIO_ENDPOINT,
            aws_access_key_id=MINIO_ROOT_USER,
            aws_secret_access_key=MINIO_ROOT_PASSWORD,
            region_name=MINIO_REGION_NAME,
            verify=False  # Set to True in production with proper certificates
        )
        return minio_client
    except Exception as e:
        raise Exception(f"Error creating MinIO client: {str(e)}")

# For backward compatibility, we'll also provide a function with the original name
get_aws_connection = get_minio_client