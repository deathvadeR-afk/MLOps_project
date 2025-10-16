# Deployment Guide

## Prerequisites

1. Docker Hub account (for container registry)
2. Cloud platform account (Render, Heroku, or AWS)
3. MongoDB Atlas account (for production database)
4. GitHub account

## Deployment Options

### Option 1: Render (Recommended for beginners)

1. Fork this repository to your GitHub account
2. Sign up at [Render](https://render.com/)
3. Connect your GitHub account to Render
4. Create a new Web Service and select your forked repository
5. Configure environment variables:
   - `MONGODB_URL`: Your MongoDB connection string
   - [MINIO_ENDPOINT](file://e:\Codecademy\MLOps\MLOps_project\src\constants\__init__.py#L24-L24): Your MinIO endpoint
   - [MINIO_ROOT_USER](file://e:\Codecademy\MLOps\MLOps_project\src\constants\__init__.py#L25-L25): MinIO username
   - [MINIO_ROOT_PASSWORD](file://e:\Codecademy\MLOps\MLOps_project\src\constants\__init__.py#L26-L26): MinIO password
6. Deploy!

### Option 2: Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t vehicle-insurance-mlops .
   ```

2. Run with environment variables:
   ```bash
   docker run -p 5000:5000 \
     -e MONGODB_URL=your_mongodb_url \
     -e MINIO_ENDPOINT=your_minio_endpoint \
     vehicle-insurance-mlops
   ```

### Option 3: Kubernetes Deployment

1. Apply the Kubernetes manifests:
   ```bash
   kubectl apply -f k8s/
   ```

2. Create secrets for sensitive data:
   ```bash
   kubectl create secret generic mongodb-secret --from-literal=url=your_mongodb_url
   kubectl create secret generic minio-secret \
     --from-literal=root-user=your_minio_user \
     --from-literal=root-password=your_minio_password
   ```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| MONGODB_URL | MongoDB connection string | Yes |
| MINIO_ENDPOINT | MinIO server endpoint | Yes |
| MINIO_ROOT_USER | MinIO username | Yes |
| MINIO_ROOT_PASSWORD | MinIO password | Yes |
| APP_HOST | Application host (default: 0.0.0.0) | No |
| APP_PORT | Application port (default: 5000) | No |

## Monitoring

The application includes health check endpoints:
- `/health` - Basic health check
- `/metrics` - (Optional) Prometheus metrics

## CI/CD Pipeline

The project includes GitHub Actions workflows:
- `.github/workflows/ci.yml` - Continuous Integration
- `.github/workflows/deploy.yml` - Continuous Deployment
- `.github/workflows/ml-pipeline.yml` - ML Pipeline Automation

To enable automatic deployment:
1. Set up secrets in your GitHub repository:
   - `DOCKER_USERNAME` - Your Docker Hub username
   - `DOCKER_PASSWORD` - Your Docker Hub password
   - `RENDER_SERVICE_ID` - Your Render service ID
   - `RENDER_API_KEY` - Your Render API key
   - `MONGODB_URL` - Your MongoDB connection string
   - `MINIO_ENDPOINT` - Your MinIO endpoint
   - `MINIO_ROOT_USER` - Your MinIO username
   - `MINIO_ROOT_PASSWORD` - Your MinIO password

## Local Development with Docker Compose

For local development and testing, you can use the provided docker-compose.yml file:

```bash
docker-compose up
```

This will start the application along with MongoDB and MinIO services.