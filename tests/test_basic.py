import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_imports():
    """Test that all main modules can be imported without errors."""
    try:
        from src.pipeline.training_pipeline import TrainPipeline
        from src.pipeline.prediction_pipeline import VehicleDataClassifier
        from src.cloud_storage.aws_storage import MinIOStorage
        assert True
    except ImportError as e:
        pytest.fail(f"Import failed: {e}")

def test_minio_storage_initialization():
    """Test that MinIO storage can be initialized."""
    try:
        from src.cloud_storage.aws_storage import MinIOStorage
        storage = MinIOStorage()
        assert storage is not None
    except Exception as e:
        pytest.fail(f"MinIOStorage initialization failed: {e}")