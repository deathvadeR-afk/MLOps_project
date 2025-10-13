"""
Main application entry point for the MLOps project.
This file serves as the central hub for running various components of the pipeline.
"""

def main():
    """Main entry point for the application."""
    print("MLOps Project Application")
    print("========================")
    print("Available commands:")
    print("1. Run full training pipeline")
    print("2. Run data ingestion")
    print("3. Run model training")
    print("4. Run model evaluation")
    print("5. Run model pusher")
    print("\nTo execute any component, run the corresponding script directly.")
    print("Example: python src/pipeline/training_pipeline.py")

if __name__ == "__main__":
    main()