# dpre.py
import pandas as pd
import sys
from sklearn.preprocessing import LabelEncoder  # Import LabelEncoder from sklearn.preprocessing
from sklearn.decomposition import PCA  # Import PCA from sklearn.decomposition
from sklearn.feature_selection import SelectKBest, f_regression  # Import SelectKBest from sklearn.feature_sele

# Load the data frame passed from the previous script
data = pd.read_csv('/home/doc-bd-a1/data_processed.csv')
# Data Cleaning
# Task 1: Remove rows with missing values
data.dropna(inplace=True)

# Task 2: Remove duplicate rows
data.drop_duplicates(inplace=True)

# Data Transformation
# Task 1: Encode categorical features (if any)
label_encoder = LabelEncoder()
data['Outcome'] = label_encoder.fit_transform(data['Outcome'])
categorical_columns = data.select_dtypes(include=['object']).columns
for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])

# Task 2: Scale numerical features (e.g., using Min-Max scaling)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
numerical_columns = data.select_dtypes(exclude=['object']).columns
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# Data Reduction
# Task 1: Principal Component Analysis (PCA) for dimensionality reduction
pca = PCA(n_components=2)
data_reduced = pca.fit_transform(data)

# Task 2: Feature selection using mutual information
X = data.drop(columns='BMI')  # Replace 'target_column' with the actual target column name
y = data['BMI']
selector = SelectKBest(score_func=f_regression, k=5)
X_new = selector.fit_transform(X, y)

# Data Discretization
# Task 1: Discretize a numerical feature into bins
data['discretized_column'] = pd.cut(data['Insulin'], bins=3, labels=["low", "medium", "high"])

# Task 2: Apply k-means clustering and use cluster labels as discrete values
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, n_init=10)
data['cluster_label'] = kmeans.fit_predict(data[['Insulin']])

# Save the preprocessed data frame as res_dpre.csv
data.to_csv('/home/doc-bd-a1/res_dpre.csv', index=False)

# Pass the data frame to the next script (eda.py) using command-line arguments
data.to_csv('/home/doc-bd-a1/data_eda.csv', index=False)
