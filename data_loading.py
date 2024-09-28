import pandas as pd
import json
import os

def load_json_data(file_paths):
    dataframes = []
    for file_path in file_paths:
        print(f"Loading JSON file: {file_path}")
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            continue

        try:
            with open(file_path, 'r') as f:
                json_data = json.load(f)
                json_df = pd.json_normalize(json_data)
                
                # Print columns and sample data for debugging
                print(f"Columns in json_df: {json_df.columns}")
                print(f"Sample data from json_df: {json_df.head()}")
                
                dataframes.append(json_df)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {file_path}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred with file {file_path}: {e}")

    return pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()

# File paths
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json', 'file5.json']

# Load data
data = load_json_data(files)
print(data.head())
