import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
def find_s_algorithm(data):
    hypotheses = ['?'] * (data.shape[1] - 1)
    for i in range(len(data)):
        if data.iloc[i, -1] == 'Malignant':
            for j in range(len(hypotheses)):
                if hypotheses[j] == '?' or hypotheses[j] == data.iloc[i, j]:
                    continue
                hypotheses[j] = '?'
    return hypotheses
data = pd.DataFrame({
    'Shape': ['Circular', 'Circular', 'Oval', 'Oval'],
    'Target': [1, 2, 3, 4],
    'Thickness': ['Thick', 'Thick', 'Thin', 'Thick'],
    'Size': ['Large', 'Large', 'Large', 'Large'],
    'Color': ['Light', 'Light', 'Dark', 'Light'],
    'Surface': ['Smooth', 'Irregular', 'Smooth', 'Irregular'],
    'Concept': ['Malignant', 'Malignant', 'Benign', 'Malignant']
})
specific_hypothesis = find_s_algorithm(data)
print(f"Most specific hypothesis: {specific_hypothesis}")
X_logistic = pd.get_dummies(data[['Target', 'Thickness', 'Size', 'Color', 'Surface']])
y_logistic = data['Concept']
logistic_model = LogisticRegression()
logistic_model.fit(X_logistic, y_logistic)
X_naive_bayes = pd.get_dummies(data[['Target', 'Thickness', 'Size', 'Color', 'Surface']])
y_naive_bayes = data['Concept']
naive_bayes_model = GaussianNB()
naive_bayes_model.fit(X_naive_bayes, y_naive_bayes)
example_data_logistic = pd.DataFrame({
    'Target': [5],
    'Thickness': ['Thin'],
    'Size': ['Large'],
    'Color': ['Dark'],
    'Surface': ['Smooth']
})
example_data_logistic_encoded = pd.get_dummies(example_data_logistic).reindex(columns=X_logistic.columns, fill_value=0)
logistic_prediction = logistic_model.predict(example_data_logistic_encoded)
print(f"Logistic Regression Prediction: {logistic_prediction}")
example_data_naive_bayes = pd.DataFrame({
    'Target': [5],
    'Thickness': ['Thin'],
    'Size': ['Large'],
    'Color': ['Dark'],
    'Surface': ['Smooth']
})
example_data_naive_bayes_encoded = pd.get_dummies(example_data_naive_bayes).reindex(columns=X_naive_bayes.columns, fill_value=0)
naive_bayes_prediction = naive_bayes_model.predict(example_data_naive_bayes_encoded)
print(f"Naive Bayes Prediction: {naive_bayes_prediction}")
