import pandas as pd
import numpy as np
def candidate_elimination(examples):
    specific_hypothesis = examples[0].copy()
    general_hypothesis = [['?' for _ in range(len(specific_hypothesis))] for _ in range(len(specific_hypothesis))]
    
    for example in examples:
        if example[-1] == 'Malignant':
            for i in range(len(specific_hypothesis)):
                if example[i] != specific_hypothesis[i]:
                    specific_hypothesis[i] = '?'
                    general_hypothesis[i][i] = '?'
        else:
            for i in range(len(specific_hypothesis)):
                if example[i] != specific_hypothesis[i]:
                    general_hypothesis[i][i] = specific_hypothesis[i]
                else:
                    general_hypothesis[i][i] = '?'
    
    return specific_hypothesis, [h for h in general_hypothesis if '?' in h]
def linear_regression(X, y):
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X, y)
    return model
def em_algorithm(data):
    
    pass
data = [
    ['Large', 'Light', 'Smooth', 'Malignant'],
    ['Large', 'Light', 'Irregular', 'Malignant'],
    ['Large', 'Dark', 'Smooth', 'Benign'],
    ['Large', 'Light', 'Irregular', 'Malignant'],
]
specific, general = candidate_elimination(data)
print("\nMost specific hypothesis:", specific)
print("Most general hypotheses:", general)
linear_data = pd.DataFrame({
    'Size': [3, 4, 5, 6],
    'Color': [1, 2, 1, 2],
    'Surface': [1, 2, 1, 2],
    'Target': [200, 300, 250, 400],
})
X_linear = linear_data.drop('Target', axis=1)
y_linear = linear_data['Target']
linear_model = linear_regression(X_linear, y_linear)
print("\nCoefficients of Linear Regression:", [linear_model.intercept_] + list(linear_model.coef_))
em_data = pd.DataFrame({
    'Feature1': [1, 2, 3, 4],
    'Feature2': [2, 3, 4, 5],
    'Label': [0, 1, 0, 1],
})
em_algorithm(em_data)

