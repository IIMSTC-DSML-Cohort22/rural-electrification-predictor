from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_results(
    X_test: pd.DataFrame,
    y_test: pd.Series,
    y_pred,
    output_dir: str,
) -> None:
    """
    Generate and save model result plots.

    Args:
        X_test (pd.DataFrame): Unscaled test features.
        y_test (pd.Series): Actual electrification percentages.
        y_pred: Predicted electrification percentages from the model.
        output_dir (str): Directory where output images will be saved.

    Returns:
        None: Saves plot files and prints confirmations.
    """
    # Ensure the output directory exists before writing image files.
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    
    