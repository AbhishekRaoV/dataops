# scripts/load_to_database.py
import pandas as pd
import sqlite3
import os

def load_to_database(data_path="data/processed/iris_processed.csv"):
    """Load processed data into SQLite database"""
    print("Starting database loading...")
    
    # Create a SQLite database
    db_path = "data/iris_database.db"
    
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    
    # Load processed data
    df = pd.read_csv(data_path)
    
    # Save to database, replacing any existing table
    df.to_sql("iris_data", conn, if_exists="replace", index=False)
    
    # Verify data was loaded correctly
    result = conn.execute("SELECT COUNT(*) FROM iris_data").fetchone()
    row_count = result[0]
    
    print(f"✅ Database loading complete. {row_count} rows loaded into {db_path}")
    print(f"Available tables: {conn.execute('SELECT name FROM sqlite_master WHERE type=\"table\"').fetchall()}")
    
    # Close connection
    conn.close()
    
    return db_path

if __name__ == "__main__":
    load_to_database()
