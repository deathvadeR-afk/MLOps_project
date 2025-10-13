import os
import sys
from src.cloud_storage.aws_storage import MinIOStorage
from src.constants import *
from src.exception import MyException
from src.logger import logging


class S3Estimator:
    """
    Class for managing model artifacts in MinIO storage (S3 compatible)
    Provides methods for saving and loading models from MinIO
    """
    
    def __init__(self):
        self.bucket_name = MODEL_BUCKET_NAME
        self.storage = MinIOStorage()
        self.model_pusher_s3_key = MODEL_PUSHER_S3_KEY
    
    def save_model(self, model_path: str, model_name: str = None):
        """
        Saves a model to MinIO storage
        :param model_path: Local path to the model file
        :param model_name: Optional name for the model in storage
        """
        try:
            if model_name is None:
                model_name = os.path.basename(model_path)
            
            # Create the S3 key (path in bucket)
            s3_key = f"{self.model_pusher_s3_key}/{model_name}"
            
            logging.info(f"Saving model {model_path} to MinIO with key {s3_key}")
            
            # Upload model to MinIO
            self.storage.upload_file(model_path, s3_key)
            
            logging.info(f"Model saved successfully to MinIO")
            return s3_key
            
        except Exception as e:
            raise MyException(e, sys) from e
    
    def load_model(self, model_name: str, local_path: str):
        """
        Loads a model from MinIO storage
        :param model_name: Name of the model in storage
        :param local_path: Local path to save the downloaded model
        """
        try:
            # Create the S3 key (path in bucket)
            s3_key = f"{self.model_pusher_s3_key}/{model_name}"
            
            logging.info(f"Loading model {model_name} from MinIO with key {s3_key}")
            
            # Download model from MinIO
            self.storage.download_file(s3_key, local_path)
            
            logging.info(f"Model loaded successfully from MinIO to {local_path}")
            return local_path
            
        except Exception as e:
            raise MyException(e, sys) from e
    
    def is_model_present(self, model_name: str):
        """
        Checks if a model exists in MinIO storage
        :param model_name: Name of the model to check
        :return: Boolean indicating if model exists
        """
        try:
            # Create the S3 key (path in bucket)
            s3_key = f"{self.model_pusher_s3_key}/{model_name}"
            
            # List files with the specific key
            files = self.storage.list_files(s3_key)
            
            return s3_key in files
            
        except Exception as e:
            raise MyException(e, sys) from e
    
    def get_latest_model_path(self):
        """
        Gets the latest model path from MinIO storage
        :return: S3 key of the latest model
        """
        try:
            # List all models in the model registry path
            files = self.storage.list_files(self.model_pusher_s3_key)
            
            if not files:
                return None
            
            # Return the latest model (you might want to implement more sophisticated logic here)
            latest_model = sorted(files)[-1] if files else None
            return latest_model
            
        except Exception as e:
            raise MyException(e, sys) from e


class Proj1Estimator(S3Estimator):
    """
    Project-specific estimator class that extends S3Estimator
    This maintains compatibility with the existing code that expects Proj1Estimator
    """
    
    def __init__(self, bucket_name: str = None, model_path: str = None):
        """
        Initialize Proj1Estimator
        :param bucket_name: Name of the bucket (optional, uses default if not provided)
        :param model_path: Path to the model in storage (optional)
        """
        # Call parent constructor
        super().__init__()
        
        # Override bucket name if provided
        if bucket_name:
            self.bucket_name = bucket_name
            
        # Store model path if provided
        self.model_path = model_path or MODEL_FILE_NAME
    
    def save_model(self, from_file: str):
        """
        Save model to MinIO storage
        :param from_file: Local path to the model file to save
        """
        try:
            # Extract model name from the provided path
            model_name = os.path.basename(from_file)
            
            # Use the parent class method to save the model
            return super().save_model(from_file, model_name)
            
        except Exception as e:
            raise MyException(e, sys) from e
    
    def load_model(self, to_file: str):
        """
        Load model from MinIO storage
        :param to_file: Local path where the model should be saved
        """
        try:
            # Extract model name from the stored model path
            model_name = os.path.basename(self.model_path)
            
            # Use the parent class method to load the model
            return super().load_model(model_name, to_file)
            
        except Exception as e:
            raise MyException(e, sys) from e
    
    def is_model_present(self, model_path: str = None):
        """
        Check if model is present in MinIO storage
        :param model_path: Path to check for model (optional, uses stored model_path if not provided)
        """
        try:
            # Use provided model path or stored one
            path_to_check = model_path or self.model_path
            model_name = os.path.basename(path_to_check)
            
            # Use the parent class method to check if model exists
            return super().is_model_present(model_name)
            
        except Exception as e:
            raise MyException(e, sys) from e