import os
import pandas as pd

def extract_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    try:
        df = pd.read_csv(path)
        if  df.empty:
            raise ValueError("Input DataFrame is empty")
        print("✅ Data extracted successfully")
        return df

    except Exception as e:
        raise RuntimeError(f"Failed to read CSV: {path}") from e
    
