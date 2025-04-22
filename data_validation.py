# scripts/data_validation.py
import pandas as pd
import json
import os

def validate_data(data_path="data/processed/iris_processed.csv"):
    """Validate the processed data against quality rules"""
    print("Starting data validation...")
    
    # Load the processed data
    df = pd.read_csv(data_path)
    
    # Define validation rules
    validation_rules = [
        {"rule": "no_missing_values", "column": "all"},
        {"rule": "value_range", "column": "sepal length (cm)", "min": -3, "max": 3},
        {"rule": "value_range", "column": "sepal width (cm)", "min": -3, "max": 3},
        {"rule": "value_range", "column": "petal length (cm)", "min": -3, "max": 3},
        {"rule": "value_range", "column": "petal width (cm)", "min": -3, "max": 3},
        {"rule": "unique_values", "column": "target", "min_unique": 3}
    ]
    
    # Run validations
    validation_results = {}
    all_passed = True
    
    for rule in validation_rules:
        if rule["rule"] == "no_missing_values":
            if rule["column"] == "all":
                has_missing = df.isnull().any().any()
                validation_results["no_missing_values"] = not has_missing
                if has_missing:
                    all_passed = False
                    print(f"❌ Validation failed: Dataset contains missing values")
        
        elif rule["rule"] == "value_range":
            col = rule["column"]
            min_val = rule["min"]
            max_val = rule["max"]
            in_range = (df[col] >= min_val).all() and (df[col] <= max_val).all()
            validation_results[f"value_range_{col}"] = in_range
            if not in_range:
                all_passed = False
                print(f"❌ Validation failed: Column '{col}' has values outside range [{min_val}, {max_val}]")
        
        elif rule["rule"] == "unique_values":
            col = rule["column"]
            min_unique = rule["min_unique"]
            unique_count = df[col].nunique()
            has_enough_unique = unique_count >= min_unique
            validation_results[f"unique_values_{col}"] = has_enough_unique
            if not has_enough_unique:
                all_passed = False
                print(f"❌ Validation failed: Column '{col}' has only {unique_count} unique values, expected at least {min_unique}")
    
    # Save validation results
    os.makedirs("reports", exist_ok=True)
    with open("reports/validation_results.json", "w") as f:
        json.dump(validation_results, f, indent=4)
    
    if all_passed:
        print("✅ All data validations passed!")
    else:
        print("❌ Some validations failed. Check reports/validation_results.json for details.")
    
    return all_passed

if __name__ == "__main__":
    validate_data()
