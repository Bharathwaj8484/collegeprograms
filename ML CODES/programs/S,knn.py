import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
def find_s_algorithm(data):
    hypothesis = ['0'] * (len(data.columns) - 1)
    for i, row in data.iterrows():
        if row.iloc[-1] == 'Yes':
            for j in range(len(hypothesis)):
                if hypothesis[j] == '0':
                    hypothesis[j] = row[j]
                elif hypothesis[j] != row[j]:
                    hypothesis[j] = '?'
    return hypothesis
find_s_data = {
    'Sky': ['sunny', 'sunny', 'rain', 'sunny'],
    'Air Temp': ['warm', 'warm', 'cold', 'warm'],
    'Humidity': ['Normal', 'High', 'High', 'High'],
    'Wind': ['Strong', 'Strong', 'Strong', 'Strong'],
    'Water': ['Warm', 'Warm', 'Warm', 'cool'],
    'Forecast': ['Same', 'Same', 'Change', 'Change'],
    'Enjoy Sport': ['Yes', 'Yes', 'No', 'Yes']
}
find_s_df = pd.DataFrame(find_s_data)
specific_hypothesis = find_s_algorithm(find_s_df)
print("\nFind-S Algorithm Output:")
print(specific_hypothesis)
linear_regression_data = {
    'Feature': [1, 2, 3, 4, 5],
    'Target': [2, 4, 5, 4, 5]
}
linear_regression_df = pd.DataFrame(linear_regression_data)
X_linear = linear_regression_df[['Feature']]
y_linear = linear_regression_df['Target']
linear_regression_model = LinearRegression()
linear_regression_model.fit(X_linear, y_linear)
print("\nLinear Regression Coefficients:")
print("Intercept:", linear_regression_model.intercept_)
print("Coefficient:", linear_regression_model.coef_[0])
knn_data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [2, 3, 4, 5, 6],
    'Target': [0, 0, 1, 1, 1]
}
knn_df = pd.DataFrame(knn_data)
X_knn = np.array(knn_df[['Feature1', 'Feature2']])
y_knn = knn_df['Target']
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_knn, y_knn)
new_data_point = np.array([[3, 4]])
knn_prediction = knn_model.predict(new_data_point)
print("\nKNN Prediction for the new data point:")
print(knn_prediction[0])
