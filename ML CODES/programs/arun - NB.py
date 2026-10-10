import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
mobile_data = {
    'Battery': [3000, 4000, 3500, 3000, 5000],
    'RAM': [4, 6, 8, 4, 6],
    'Storage': [64, 128, 64, 32, 128],
    'Price Range': [1, 2, 2, 1, 3]}
mobile_df = pd.DataFrame(mobile_data)
print("First five rows of the dataset:")
print(mobile_df.head())
print("\nBasic statistical computations:")
print(mobile_df.describe())
print("\nColumns and their data types:")
print(mobile_df.dtypes)
print("\nNull values before replacement:")
print(mobile_df.isnull().sum())
mobile_df.fillna(mobile_df.mode().iloc[0], inplace=True)
print("\nNull values after replacement:")
print(mobile_df.isnull().sum())
print("\nHeatmap of the dataset:")
sns.heatmap(mobile_df.corr(), annot=True, cmap='coolwarm')
plt.show()
X = mobile_df.drop('Price Range', axis=1)
y = mobile_df['Price Range']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
naive_bayes_classifier = GaussianNB()
naive_bayes_classifier.fit(X_train, y_train)
y_pred = naive_bayes_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy of the Naive Bayes Classifier: {accuracy:.2f}")
