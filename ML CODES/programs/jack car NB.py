import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt
car_data = {
    'Make': ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan'],
    'Model': ['Camry', 'Civic', 'Fusion', 'Malibu', 'Altima'],
    'Year': [2018, 2017, 2019, 2018, 2017],
    'Engine_Size': [2.5, 2.0, 2.0, 1.5, 2.5],
    'Number_of_Doors': [4, 4, 4, 4, 4],
    'Sale_Price': [25000, 22000, 23000, 20000, 24000]
}
df = pd.DataFrame(car_data)
print("First five rows of the dataset:")
print(df.head())
print("\nBasic statistical computations:")
print(df.describe())
print("\nColumns and their data types:")
print(df.dtypes)
df.loc[2, 'Engine_Size'] = None  
imputer = SimpleImputer(strategy='most_frequent')
df['Engine_Size'] = imputer.fit_transform(df[['Engine_Size']])
print("\nHeatmap of the numeric columns:")
numeric_columns = df.select_dtypes(include=['number']).columns
sns.heatmap(df[numeric_columns].corr(), annot=True, cmap='coolwarm', linewidths=.5)
plt.show()
X = df[['Year', 'Engine_Size', 'Number_of_Doors']]
y = df['Sale_Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error (MSE) of the Linear Regression model:")
print(accuracy)
