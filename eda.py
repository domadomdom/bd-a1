# eda.py
import pandas as pd

# Load the data frame passed from the previous script
data = pd.read_csv('/home/doc-bd-a1/data_eda.csv')

# Perform exploratory data analysis and generate insights
# 1st Insight
insight1 = "The mean age of patients in the dataset is {:.2f} years.".format(data['Age'].mean())

# 2nd Insight
insight2 = "The maximum blood pressure in the dataset is {} mm Hg.".format(data['BloodPressure'].max())

# 3rd Insight
insight3 = "There are {} unique values in the 'Outcome' column.".format(data['Outcome'].nunique())

# Save insights as text files
with open("eda-in-1.txt", "w") as file1:
    file1.write(insight1)

with open("eda-in-2.txt", "w") as file2:
    file2.write(insight2)

with open("eda-in-3.txt", "w") as file3:
    file3.write(insight3)

# Pass the data frame to the next script (vis.py) using command-line arguments
data.to_csv('/home/doc-bd-a1/data_vis.csv', index=False)

