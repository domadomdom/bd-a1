import pandas as pd
from sklearn.cluster import KMeans

# Load the data frame passed from the previous script (vis.py)
data = pd.read_csv('/home/doc-bd-a1/data_vis.csv')

# Define the columns you want to use for K-means clustering (customize as needed)
# In this example, we'll use 'Feature A' and 'Feature B'.
features = data[['Age', 'BMI']]

# Set the number of clusters (k) for K-means
k = 3

# Perform K-means clustering
kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
data['cluster_label'] = kmeans.fit_predict(features)

# Save the number of records in each cluster as a text file (k.txt)
cluster_counts = data['cluster_label'].value_counts().sort_index()
cluster_counts.to_csv('/home/doc-bd-a1/k.txt', header=True, index_label='Cluster')

