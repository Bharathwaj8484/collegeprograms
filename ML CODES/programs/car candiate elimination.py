import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
def candidate_elimination(training_data):
    specific_hypothesis = ["0"] * (len(training_data.columns) - 1)
    general_hypothesis = ["?"] * (len(training_data.columns) - 1)
    for index, row in training_data.iterrows():
        if row['Example type'] == 'Positive':
            for i in range(len(row) - 1):
                if specific_hypothesis[i] == "0":
                    specific_hypothesis[i] = row[i]
                elif specific_hypothesis[i] != row[i]:
                    specific_hypothesis[i] = "?"

            for i in range(len(row) - 1):
                if general_hypothesis[i] != specific_hypothesis[i] and general_hypothesis[i] != "?":
                    general_hypothesis[i] = "?"
        elif row['Example type'] == 'Negative':
            for i in range(len(row) - 1):
                if specific_hypothesis[i] == row[i]:
                    specific_hypothesis[i] = "?"

            for i in range(len(row) - 1):
                if specific_hypothesis[i] != "?" and general_hypothesis[i] != "?" and specific_hypothesis[i] != general_hypothesis[i]:
                    temp = general_hypothesis[i]
                    general_hypothesis[i] = specific_hypothesis[i]
                    general_hypothesis[i] = temp

    return specific_hypothesis, general_hypothesis
def polynomial_regression(X, y, degree):
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)
    return model
data = {
    'Origin': ['Japan', 'Japan', 'Japan', 'USA', 'Japan'],
    'Manufacturer': ['Honda', 'Toyota', 'Toyota', 'Chrysler', 'Honda'],
    'Color': ['Blue', 'Green', 'Blue', 'Red', 'White'],
    'Decade': [1980, 1970, 1990, 1980, 1980],
    'Type': ['Economy', 'Sports', 'Economy', 'Economy', 'Economy'],
    'Example type': ['Positive', 'Negative', 'PositiveNegative', 'Positive', 'Positive']
}
df = pd.DataFrame(data)
specific, general = candidate_elimination(df)
print("\nCandidate-Elimination Algorithm Results:")
print("Specific Hypothesis:", specific)
print("General Hypothesis:", general)
X_poly = df[['Decade']]
y_poly = df['Decade']  
degree_poly = 2
model_poly = polynomial_regression(X_poly, y_poly, degree_poly)
print("\nCoefficients of Polynomial Regression:", model_poly.coef_[1:])  
