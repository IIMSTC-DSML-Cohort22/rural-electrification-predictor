"""
Rural Electrification Predictor - Main Pipeline
SDG 9: Predicting Rural Electrification using Data Analysis and Linear Regression
"""

import sys
from pathlib import Path

# Add src directory to Python path
sys.path.append(str(Path(__file__).parent / "src"))

from Data_Cleaning import clean_dataset
from Data_preprocessing import preprocess
from eda import run_eda
from Model import train_and_evaluate


def main():
    """
    Execute the complete rural electrification prediction pipeline.
    
    Pipeline Steps:
    1. Data Cleaning - Handle missing values, outliers, and data types
    2. Exploratory Data Analysis - Visualize patterns and relationships
    3. Data Preprocessing - Feature scaling and train-test split
    4. Model Training & Evaluation - Linear regression with performance metrics
    """
    print("=" * 70)
    print("RURAL ELECTRIFICATION PREDICTOR - PIPELINE EXECUTION")
    print("=" * 70)
    
    # Define file paths
    raw_data_path = "Data/data.csv"
    cleaned_data_path = "Data/cleaned_data.csv"
    
    # Step 1: Data Cleaning
    print("\n[STEP 1/4] DATA CLEANING")
    print("-" * 70)
    df_cleaned = clean_dataset(raw_data_path, cleaned_data_path)
    
    # Step 2: Exploratory Data Analysis
    print("\n[STEP 2/4] EXPLORATORY DATA ANALYSIS")
    print("-" * 70)
    run_eda(df_cleaned)
    
    # Step 3: Data Preprocessing
    print("\n[STEP 3/4] DATA PREPROCESSING")
    print("-" * 70)
    X_train_scaled, X_test_scaled, X_train, X_test, y_train, y_test, scaler = preprocess(df_cleaned)
    
    # Step 4: Model Training and Evaluation
    print("\n[STEP 4/4] MODEL TRAINING & EVALUATION")
    print("-" * 70)
    train_and_evaluate(X_train_scaled, X_test_scaled, X_train, X_test, y_train, y_test)
    
    print("\n" + "=" * 70)
    print("PIPELINE EXECUTION COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()
