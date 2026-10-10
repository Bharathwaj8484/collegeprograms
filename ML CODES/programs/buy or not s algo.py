import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.mixture import GaussianMixture
def find_s_algorithm(examples):
    hypothesis = ['?'] * (len(examples.columns) - 1)
    for index, row in examples.iterrows():
        if row.iloc[-1] == 'Yes':
            for i in range(len(hypothesis)):
                if hypothesis[i] == '?':
                    hypothesis[i] = row.iloc[i]
                elif hypothesis[i] != row.iloc[i]:
                    hypothesis[i] = '?'
    return hypothesis
data = {
    'Citations': [1, 2, 3, 4],
    'Size': ['Small', 'Medium', 'Small', 'Small'],
    'InLibra': ['No', 'No', 'No', 'No'],
    'Price': ['Affordable', 'Expensive', 'Expensive', 'Affordable'],
    'Editions': ['Few', 'Many', 'Few', 'Many'],
    'Buy': ['No', 'Yes', 'Yes', 'Yes']}

df = pd.DataFrame(data)
hypothesis = find_s_algorithm(df)
print("Most specific hypothesis (Find-S Algorithm):", hypothesis)
le = LabelEncoder()
df['Size'] = le.fit_transform(df['Size'])
df['Buy'] = le.fit_transform(df['Buy'])  
X_linear = df[['Citations', 'Size']]
y_linear = df['Buy']
X_train_linear, X_test_linear, y_train_linear, y_test_linear = train_test_split(X_linear, y_linear, test_size=0.25, random_state=42)
linear_model = LinearRegression()
linear_model.fit(X_train_linear, y_train_linear)
logistic_model = LogisticRegression()
logistic_model.fit(X_train_linear, y_train_linear)
linear_predictions = linear_model.predict(X_test_linear)
logistic_predictions = logistic_model.predict(X_test_linear)
linear_mse = mean_squared_error(y_test_linear, linear_predictions)
logistic_accuracy = accuracy_score(y_test_linear, logistic_predictions)
print("Linear Regression MSE:", linear_mse)
print("Logistic Regression Accuracy:", logistic_accuracy)
