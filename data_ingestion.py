# scripts/data_ingestion.py
import pandas as pd
import os
from sklearn.datasets import load_iris

def ingest_data():
    """Download sample data (Iris dataset) for the POC"""
    print("Starting data ingestion...")
    
    # Create raw data directory if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)
    
    # Load Iris dataset as an example
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    
    # Save as CSV in the raw data directory
    output_path = "data/raw/iris_data.csv"
    df.to_csv(output_path, index=False)
    
    print(f"Data ingestion complete. Data saved to {output_path}")
    print(f"Downloaded {len(df)} records with {len(df.columns)} columns")
    
    return output_path

if __name__ == "__main__":
    ingest_data()
