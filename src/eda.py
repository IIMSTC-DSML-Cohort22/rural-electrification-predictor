import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def run_eda(df: pd.DataFrame) -> None:
    """
    Perform exploratory analysis and visual inspection of cleaned data.

    Args:
        df (pd.DataFrame): Cleaned dataset to analyze.

    Returns:
        None: This function prints outputs and displays plots.
    """
    # Step 1: Print descriptive statistics to summarize numeric distributions.
    print("\nDescriptive Statistics:")
    print(df.describe())

    # Step 2: Print DataFrame schema to inspect types and non-null counts.
    print("\nDataFrame Info:")
    df.info()

    # Step 3: Plot distance from grid versus electrification percentage.
    plt.figure(figsize=(10, 6))
    plt.scatter(df["distance_from_grid_km"], df["electrification_pct"], alpha=0.7)
    plt.title("Distance from Grid vs. Electrification %")
    plt.xlabel("Distance from Grid (km)")
    plt.ylabel("Electrification (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
