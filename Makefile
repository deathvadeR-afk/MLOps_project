# Makefile for Vehicle Insurance MLOps Project

# Variables
PYTHON = python
PIP = pip
DOCKER = docker

# Default target
.PHONY: help
help:
	@echo "Vehicle Insurance MLOps Project - Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make setup              Install dependencies"
	@echo "  make run                Start the FastAPI application"
	@echo "  make train              Run the complete MLOps pipeline"
	@echo "  make test               Run all tests"
	@echo "  make minio              Start MinIO server"
	@echo "  make docker-build       Build Docker image"
	@echo "  make docker-run         Run Docker container"
	@echo "  make clean              Clean up artifacts"

# Setup environment
.PHONY: setup
setup:
	$(PIP) install -r requirements.txt

# Run the FastAPI application
.PHONY: run
run:
	$(PYTHON) app.py

# Run the complete MLOps pipeline
.PHONY: train
train:
	$(PYTHON) demo.py

# Run tests
.PHONY: test
test:
	$(PYTHON) -m pytest tests/

# Start MinIO server
.PHONY: minio
minio:
	$(DOCKER) run -p 9000:9000 -p 9001:9001 minio/minio server /data --console-address ":9001"

# Build Docker image
.PHONY: docker-build
docker-build:
	$(DOCKER) build -t vehicle-insurance-mlops .

# Run Docker container
.PHONY: docker-run
docker-run:
	$(DOCKER) run -p 5000:5000 vehicle-insurance-mlops

# Clean up artifacts
.PHONY: clean
clean:
	rm -rf artifact/
	rm -rf logs/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete