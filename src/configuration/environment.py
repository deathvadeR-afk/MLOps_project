import os
from typing import Optional
from datetime import datetime

class EnvironmentConfig:
    """Environment configuration class"""
    
    @staticmethod
    def get_mongodb_url() -> str:
        """Get MongoDB URL from environment or return default"""
        return os.getenv("MONGODB_URL", "mongodb://localhost:27017/Proj1")
    
    @staticmethod
    def get_minio_endpoint() -> str:
        """Get MinIO endpoint from environment or return default"""
        return os.getenv("MINIO_ENDPOINT", "http://localhost:9000")
    
    @staticmethod
    def get_minio_credentials() -> tuple:
        """Get MinIO credentials from environment or return defaults"""
        user = os.getenv("MINIO_ROOT_USER", "minioadmin")
        password = os.getenv("MINIO_ROOT_PASSWORD", "minioadmin")
        return user, password
    
    @staticmethod
    def get_app_host() -> str:
        """Get application host from environment or return default"""
        return os.getenv("APP_HOST", "0.0.0.0")
    
    @staticmethod
    def get_app_port() -> int:
        """Get application port from environment or return default"""
        return int(os.getenv("APP_PORT", "5000"))