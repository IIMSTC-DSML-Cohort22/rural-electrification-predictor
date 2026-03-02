from pathlib import Path
from src.data_cleaning import clean_dataset
import pandas as pd
from src.eda import run_eda
from src.model import train_and_evaluate
from src.preprocessing import preprocess
from src.visualization import plot_results


def main() -> None:
    """
    Run all project steps in sequence from data generation to visualization.

    Returns:
        None: Executes the pipeline and prints progress/results.
    """
    # Print startup banner for the project pipeline.
    print("=" * 60)
    print("  Bangalore Rural Electrification Predictor")
    print("  Mini Project Pipeline")
    print("=" * 60)

    # Define all required input and output paths relative to project root.
    project_root = Path(__file__).resolve().parent
    raw_data_path = project_root / "Data" / "data.csv"
    output_dir = project_root / "outputs"

    