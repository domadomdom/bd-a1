# load.py
import pandas as pd
import sys

# Accept the dataset file path as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python load.py <dataset_file>")
    sys.exit(1)

dataset_file = sys.argv[1]

# Load the dataset
data = pd.read_csv(dataset_file)

# Pass the data frame to the next script (dpre.py) using command-line arguments
data.to_csv('/home/doc-bd-a1/data_processed.csv', index=False)  # Save data as a CSV for the next script
