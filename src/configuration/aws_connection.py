import boto3
import os
from src.constants import *
from src.configuration.environment import EnvironmentConfig

def get_minio_client():
    """
    Creates and returns a MinIO client using boto3 (S3 compatible API)
    MinIO is used as an alternative to AWS S3 for local model storage
    """
    try:
        # Get MinIO configuration from environment
        minio_endpoint = EnvironmentConfig.get_minio_endpoint()
        minio_user, minio_password = EnvironmentConfig.get_minio_credentials()
        
        # Create a boto3 client configured for MinIO
        minio_client = boto3.client(
            's3',
            endpoint_url=minio_endpoint,
            aws_access_key_id=minio_user,
            aws_secret_access_key=minio_password,
            region_name=MINIO_REGION_NAME,
            verify=False  # Set to True in production with proper certificates
        )
        return minio_client
    except Exception as e:
        raise Exception(f"Error creating MinIO client: {str(e)}")

# For backward compatibility, we'll also provide a function with the original name
get_aws_connection = get_minio_client