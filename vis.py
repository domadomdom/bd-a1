import matplotlib.pyplot as plt
import pandas as pd

# Load the data frame passed from the previous script (eda.py)
data = pd.read_csv('/home/doc-bd-a1/data_vis.csv')

# Create a simple scatter plot as an example visualization
plt.scatter(data['Age'], data['BMI'])
plt.xlabel('Age')
plt.ylabel('BMI')
plt.title('Scatter Plot of Age vs. BMI')

# Save the visualization as vis.png
plt.savefig('/home/doc-bd-a1/vis.png')

# Optionally, display the visualization (you can remove this line if not needed)
plt.show()

