# Vehicle Insurance Prediction MLOps Project

An end-to-end MLOps solution for predicting vehicle insurance responses using machine learning with local MinIO storage instead of AWS S3.

## Project Overview

This project implements a complete MLOps pipeline for a vehicle insurance prediction model. It includes data ingestion from MongoDB, data validation, transformation, model training, evaluation, and deployment. The system uses MinIO as a local S3-compatible storage alternative, eliminating the need for AWS cloud services.

## Tech Stack

### Core Technologies
- **Python 3.10** - Primary programming language
- **FastAPI** - Web framework for API development
- **Scikit-learn** - Machine learning library
- **MongoDB** - Database for storing raw data
- **MinIO** - Local S3-compatible object storage
- **Docker** - Containerization platform

### Key Libraries
- **pandas/numpy** - Data manipulation and numerical computing
- **scikit-learn** - Machine learning algorithms
- **imblearn** - Handling imbalanced datasets
- **boto3** - AWS SDK (configured for MinIO)
- **PyYAML** - Configuration management
- **dill** - Extended pickle module for object serialization
- **Jinja2** - Template engine for web interface

### MLOps Components
- **Data Ingestion** - Fetches data from MongoDB
- **Data Validation** - Validates data quality and schema
- **Data Transformation** - Preprocesses and transforms data
- **Model Training** - Trains machine learning model
- **Model Evaluation** - Compares model performance
- **Model Pusher** - Deploys model to production storage

## Architecture

```
┌─────────────┐    ┌──────────────┐    ┌─────────────────┐
│   MongoDB   │───▶│ Data Ingestion├───▶│ Data Validation │
└─────────────┘    └──────────────┘    └─────────────────┘
                                            │
                                            ▼
┌─────────────┐    ┌─────────────────┐    ┌──────────────────┐
│    MinIO    │◀───┤ Model Registry  │◀───┤ Model Evaluation │
└─────────────┘    └─────────────────┘    └──────────────────┘
       ▲                                     ▲        ▲
       │                                     │        │
┌──────────────┐                      ┌──────────────┐│
│ Web Interface│                      │ Model Trainer ││
└──────────────┘                      └──────────────┘│
       │                                     │        │
       ▼                                     ▼        │
┌──────────────┐    ┌─────────────────┐    ┌──────────────────┐
│   FastAPI    │───▶│ Data Transform. ├───▶│ Model Deployment │
└──────────────┘    └─────────────────┘    └──────────────────┘
```

## Prerequisites

- Python 3.10
- Docker (for MinIO)
- MongoDB instance
- Conda or virtual environment

## Setup Instructions

### 1. Environment Setup
```bash
# Create conda environment
conda create -n vehicle python=3.10 -y
conda activate vehicle

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file with your MongoDB connection string:
```env
MONGODB_URL=your_mongodb_connection_string
```

### 3. Start MinIO Server

On Unix/Linux/macOS:
```bash
# Run MinIO using Docker
docker run -p 9000:9000 -p 9001:9001 minio/minio server /data --console-address ":9001"
```

On Windows, you can use the provided batch script:
```bash
start-minio.bat
```

MinIO will be accessible at:
- API: http://localhost:9000
- Console: http://localhost:9001
- Default credentials: minioadmin/minioadmin

### 4. Run the Application
```bash
# Start the FastAPI application
python app.py
```

The application will be available at: http://127.0.0.1:5000

## Usage

### Web Interface
- Access the main page at http://127.0.0.1:5000 to input vehicle data and get predictions
- Use the `/train` endpoint to trigger the complete MLOps pipeline

### Training Pipeline
```bash
# Run the complete MLOps pipeline
python demo.py
```

### Docker Deployment
```bash
# Build and run with Docker
docker build -t vehicle-insurance-mlops .
docker run -p 5000:5000 vehicle-insurance-mlops
```

## Testing

Run tests using pytest:
```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_basic.py

# Run tests with verbose output
python -m pytest -v tests/
```

## Project Structure
```
├── app.py                 # FastAPI web application
├── demo.py                # Pipeline execution script
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── src/
│   ├── components/        # MLOps pipeline components
│   ├── entity/            # Configuration and artifact entities
│   ├── pipeline/          # Training and prediction pipelines
│   ├── cloud_storage/     # MinIO storage implementation
│   ├── configuration/     # Connection configurations
│   ├── constants/         # Project constants
│   ├── data_access/       # Database access layer
│   ├── exception/         # Custom exception handling
│   ├── logger/            # Logging configuration
│   └── utils/             # Utility functions
└── templates/             # HTML templates
```

## Key Features

1. **Cloud-Free Operation**: Uses MinIO instead of AWS S3 for local model storage
2. **Complete MLOps Pipeline**: End-to-end workflow from data to deployment
3. **Model Registry**: Stores and manages trained models in MinIO
4. **Web Interface**: User-friendly interface for predictions
5. **Containerization**: Docker support for easy deployment
6. **Modular Architecture**: Well-organized codebase for maintainability

## Development

### Running Tests
```bash
# Run specific component tests
python -m pytest tests/
```

### Using Makefile (Unix/Linux/macOS)
```bash
# Install dependencies
make setup

# Start the application
make run

# Run the complete pipeline
make train

# Run tests
make test

# Start MinIO
make minio

# Build and run Docker container
make docker-build
make docker-run
```

### Extending the Pipeline
1. Add new components in `src/components/`
2. Update configurations in `src/entity/config_entity.py`
3. Integrate new components in `src/pipeline/training_pipeline.py`

## CI/CD Pipeline

This project includes a complete CI/CD pipeline using GitHub Actions:

- **Continuous Integration**: Runs tests and linting on every push
- **Continuous Deployment**: Automatically deploys to cloud platforms
- **ML Pipeline Automation**: Scheduled model training and evaluation

To enable the CI/CD pipeline:

1. Fork this repository to your GitHub account
2. Set up the required secrets in your repository settings:
   - `DOCKER_USERNAME` - Your Docker Hub username
   - `DOCKER_PASSWORD` - Your Docker Hub password
   - `RENDER_SERVICE_ID` - Your Render service ID (if using Render)
   - `RENDER_API_KEY` - Your Render API key (if using Render)
   - `MONGODB_URL` - Your MongoDB connection string
   - `MINIO_ENDPOINT` - Your MinIO endpoint
   - `MINIO_ROOT_USER` - Your MinIO username
   - `MINIO_ROOT_PASSWORD` - Your MinIO password

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.