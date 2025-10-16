import pytest
import os
from src.configuration.environment import EnvironmentConfig

def test_get_mongodb_url_default():
    """Test that get_mongodb_url returns default value when no env var is set"""
    # Unset the environment variable if it exists
    old_value = os.environ.pop('MONGODB_URL', None)
    
    try:
        url = EnvironmentConfig.get_mongodb_url()
        assert url == "mongodb://localhost:27017/Proj1"
    finally:
        # Restore the environment variable if it existed
        if old_value:
            os.environ['MONGODB_URL'] = old_value

def test_get_mongodb_url_from_env():
    """Test that get_mongodb_url returns value from environment variable"""
    # Set a test value
    old_value = os.environ.get('MONGODB_URL')
    os.environ['MONGODB_URL'] = "mongodb://test:1234/testdb"
    
    try:
        url = EnvironmentConfig.get_mongodb_url()
        assert url == "mongodb://test:1234/testdb"
    finally:
        # Restore the original value
        if old_value:
            os.environ['MONGODB_URL'] = old_value
        elif 'MONGODB_URL' in os.environ:
            del os.environ['MONGODB_URL']

def test_get_minio_endpoint_default():
    """Test that get_minio_endpoint returns default value when no env var is set"""
    # Unset the environment variable if it exists
    old_value = os.environ.pop('MINIO_ENDPOINT', None)
    
    try:
        endpoint = EnvironmentConfig.get_minio_endpoint()
        assert endpoint == "http://localhost:9000"
    finally:
        # Restore the environment variable if it existed
        if old_value:
            os.environ['MINIO_ENDPOINT'] = old_value

def test_get_minio_credentials_default():
    """Test that get_minio_credentials returns default values when no env vars are set"""
    # Unset the environment variables if they exist
    old_user = os.environ.pop('MINIO_ROOT_USER', None)
    old_password = os.environ.pop('MINIO_ROOT_PASSWORD', None)
    
    try:
        user, password = EnvironmentConfig.get_minio_credentials()
        assert user == "minioadmin"
        assert password == "minioadmin"
    finally:
        # Restore the environment variables if they existed
        if old_user:
            os.environ['MINIO_ROOT_USER'] = old_user
        if old_password:
            os.environ['MINIO_ROOT_PASSWORD'] = old_password

def test_get_app_host_default():
    """Test that get_app_host returns default value when no env var is set"""
    # Unset the environment variable if it exists
    old_value = os.environ.pop('APP_HOST', None)
    
    try:
        host = EnvironmentConfig.get_app_host()
        assert host == "0.0.0.0"
    finally:
        # Restore the environment variable if it existed
        if old_value:
            os.environ['APP_HOST'] = old_value

def test_get_app_port_default():
    """Test that get_app_port returns default value when no env var is set"""
    # Unset the environment variable if it exists
    old_value = os.environ.pop('APP_PORT', None)
    
    try:
        port = EnvironmentConfig.get_app_port()
        assert port == 5000
    finally:
        # Restore the environment variable if it existed
        if old_value:
            os.environ['APP_PORT'] = old_value