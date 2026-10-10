import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
def find_s_algorithm(dataset):
    hypothesis = ["0"] * (len(dataset[0]) - 1)
    
    for example in dataset:
        if example[-1] == "Positive":
            for i in range(len(example) - 1):
                if hypothesis[i] == "0":
                    hypothesis[i] = example[i]
                elif hypothesis[i] != example[i]:
                    hypothesis[i] = "?"
    
    return hypothesis
def polynomial_regression(X, y, degree):
    poly = PolynomialFeatures(degree)
    X_poly = poly.fit_transform(X)
    
    model = LinearRegression()
    model.fit(X_poly, y)
    
    return model.coef_[1:]  
def knn_algorithm(X, y, k):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(X_train, y_train)
    
    y_pred = knn_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy
dataset = [
    ["Japan", "honda", "Blue", "1980", "Economy", "Positive"],
    ["Japan", "toyota", "Green", "1970", "Sports", "Negative"],
    ["Japan", "toyota", "Blue", "1990", "Economy", "PositiveNegative"],
    ["USA", "chrysler", "Red", "1980", "Economy", "Positive"],
    ["Japan", "honda", "White", "1980", "Economy", "Positive"]
]
result_hypothesis = find_s_algorithm(dataset)
print("Most specific hypothesis:", result_hypothesis)
X_poly = np.array([[1], [2], [3], [4], [5]])
y_poly = np.array([2, 8, 18, 32, 50])
degree_poly = 2
poly_coefficients = polynomial_regression(X_poly, y_poly, degree_poly)
print("Coefficients of Polynomial Regression:", poly_coefficients)
X_knn = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y_knn = np.array([0, 1, 0, 1])
k_knn = 3
accuracy_knn = knn_algorithm(X_knn, y_knn, k_knn)
print("Accuracy of KNN:", accuracy_knn)
