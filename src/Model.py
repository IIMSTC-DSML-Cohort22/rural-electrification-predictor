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
    # Step 1: Train a linear regression model on scaled feature inputs.
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Step 2: Print intercept and coefficients to inspect learned linear weights.
    print("\nModel Parameters:")
    print(f"Intercept: {model.intercept_:.4f}")
    print("Coefficients:")
    print(f"  distance_from_grid_km: {model.coef_[0]:.4f}")
    print(f"  pop_density: {model.coef_[1]:.4f}")

    # Step 3: Predict electrification percentages for the test feature set.
    y_pred = model.predict(X_test_scaled)