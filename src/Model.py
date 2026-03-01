import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def train_and_evaluate(
    X_train_scaled,
    X_test_scaled,
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
):
    """
    Train a linear regression model and evaluate predictive performance.

    Args:
        X_train_scaled: Scaled training features.
        X_test_scaled: Scaled testing features.
        X_train (pd.DataFrame): Unscaled training features.
        X_test (pd.DataFrame): Unscaled testing features.
        y_train (pd.Series): Training target values.
        y_test (pd.Series): Testing target values.

    Returns:
        tuple: Trained model and predicted test values (model, y_pred).
    """