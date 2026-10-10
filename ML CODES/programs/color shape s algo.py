import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
def find_s_algorithm(data):
    specific_hypothesis = ['?'] * (len(data.columns) - 1)
    for index, row in data.iterrows():
        if row.iloc[-1] == 1:
            for i in range(len(row) - 1):
                if specific_hypothesis[i] == '?':
                    specific_hypothesis[i] = row.iloc[i]
                elif specific_hypothesis[i] != row.iloc[i]:
                    specific_hypothesis[i] = '?'
    return specific_hypothesis
def polynomial_regression(X, y, degree):
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)
    return model
def knn_algorithm(X_train, y_train, X_test, k):
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(X_train, y_train)
    y_pred = knn_model.predict(X_test)
    return y_pred
data = pd.DataFrame({
    'Size': ['Small', 'Small', 'Small', 'Large', 'Large'],
    'Color': ['Red', 'Red', 'Red', 'Blue', 'Blue'],
    'Shape': ['Circle', 'Triangle', 'Circle', 'Circle', 'Circle'],
    'Class': [1, 0, 1, 0, 1]  
})
specific_hypothesis = find_s_algorithm(data)
print("\nMost specific hypothesis (Find-S Algorithm):", specific_hypothesis)
X_poly = pd.get_dummies(data[['Size', 'Color', 'Shape']])
y_poly = data['Class']
poly_model = polynomial_regression(X_poly, y_poly, degree=2)
print("\nCoefficients of Polynomial Regression:", poly_model.coef_)
X_knn = pd.get_dummies(data[['Size', 'Color', 'Shape']])
y_knn = data['Class']
X_train_knn, X_test_knn, y_train_knn, y_test_knn = train_test_split(X_knn, y_knn, test_size=0.2, random_state=42)
knn_predictions = knn_algorithm(X_train_knn, y_train_knn, X_test_knn, k=3)
accuracy_knn = accuracy_score(y_test_knn, knn_predictions)
print("\nAccuracy of KNN Algorithm:", accuracy_knn)
