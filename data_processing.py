# scripts/data_processing.py
import pandas as pd
import os
import numpy as np

def process_data(input_path="data/raw/iris_data.csv"):
    """Process the raw data by normalizing features and basic transformations"""
    print("Starting data processing...")
    
    # Create processed data directory if it doesn't exist
    os.makedirs("data/processed", exist_ok=True)
    
    # Load the raw data
    df = pd.read_csv(input_path)
    print(f"Loaded raw data with shape: {df.shape}")
    
    # Simple data processing steps
    # 1. Normalize numerical features
    feature_columns = [col for col in df.columns if col != 'target']
    for column in feature_columns:
        df[column] = (df[column] - df[column].mean()) / df[column].std()
    
    # 2. Add a simple feature - combination of features
    df['combined_feature'] = df[feature_columns].mean(axis=1)
    
    # Save processed data
    output_path = "data/processed/iris_processed.csv"
    df.to_csv(output_path, index=False)
    
    print(f"Data processing complete. Processed data saved to {output_path}")
    return output_path

if __name__ == "__main__":
    process_data()
