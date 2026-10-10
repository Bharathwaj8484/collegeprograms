import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import LabelEncoder
def candidate_elimination(training_data):
    hypotheses = [({}, {})]
    
    for example in training_data:
        input_data, output_data = example[:-1], example[-1]
        
        if output_data == 'Yes':
            for i in range(len(hypotheses)):
                for j in range(len(input_data)):
                    if hypotheses[i][0].get(j, None) is None:
                        hypotheses[i][0][j] = input_data[j]
                    elif hypotheses[i][0][j] != input_data[j]:
                        hypotheses[i][0][j] = '?'
                    
        elif output_data == 'No':
            new_hypotheses = []
            for i in range(len(hypotheses)):
                temp_hypothesis = hypotheses[i][0].copy()
                for j in range(len(input_data)):
                    if input_data[j] != hypotheses[i][0].get(j, None):
                        temp_hypothesis[j] = hypotheses[i][0].get(j, input_data[j])
                        new_hypotheses.append((temp_hypothesis.copy(), {}))
            hypotheses = new_hypotheses
            
    return hypotheses
training_data = [
    ('sunny', 'warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'),
    ('sunny', 'warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'),
    ('rain', 'cold', 'High', 'Strong', 'Warm', 'Change', 'No'),
    ('sunny', 'warm', 'High', 'Strong', 'cool', 'Change', 'Yes')
]
result_hypotheses = candidate_elimination(training_data)
print("\nCandidate-Elimination Algorithm Output:")
print(result_hypotheses)
logistic_regression_data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [2, 3, 4, 5, 6],
    'Target': [0, 0, 1, 1, 1]
}
logistic_regression_df = pd.DataFrame(logistic_regression_data)
X_logistic = logistic_regression_df[['Feature1', 'Feature2']]
y_logistic = logistic_regression_df['Target']
logistic_regression_model = LogisticRegression()
logistic_regression_model.fit(X_logistic, y_logistic)
print("\nLogistic Regression Coefficients:")
print("Intercept:", logistic_regression_model.intercept_[0])
print("Coefficient:", logistic_regression_model.coef_[0])
em_data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [2, 3, 4, 5, 6]
}
em_df = pd.DataFrame(em_data)
em_model = GaussianMixture(n_components=2)
em_model.fit(em_df)
print("\nExpectation Maximization (EM) Algorithm Parameters:")
print("Weights:", em_model.weights_)
print("Means:", em_model.means_)
print("Covariances:", em_model.covariances_)
