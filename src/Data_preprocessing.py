from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocess(
    df: pd.DataFrame,
) -> Tuple:
    """
    Prepare model features and target with train-test split and scaling.

    Args:
        df (pd.DataFrame): Cleaned dataset for machine learning preparation.

    Returns:
        tuple: X_train_scaled, X_test_scaled, X_train, X_test, y_train, y_test, scaler
    """
    # Step 1: Select model features tied to grid distance and village density.
    X = df[["distance_from_grid_km", "pop_density"]]

    # Step 2: Select target variable as electrification percentage.
    y = df["electrification_pct"]

    