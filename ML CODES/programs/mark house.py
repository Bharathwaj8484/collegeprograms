import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
house_data = pd.DataFrame({
    'area': [2000, 1600, 1800, 1400, 1200],  
    'bedrooms': [3, 4, 3, 2, 2],  
    'bathrooms': [2, 2, 1, 1, 1],  
    'price': [300000, 400000, 250000, 200000, 180000]  
})
print("1st five rows of the dataset:")
print(house_data.head())
print("\nBasic statistical computations:")
print(house_data.describe())
print("\nColumns and their data types:")
print(house_data.dtypes)
print("\nNull values before replacement:")
print(house_data.isnull().sum())
imputer = SimpleImputer(strategy='most_frequent')
house_data_imputed = pd.DataFrame(imputer.fit_transform(house_data), columns=house_data.columns)
print("\nNull values after replacement:")
print(house_data_imputed.isnull().sum())
print("\nHeatmap of the numeric columns:")
sns.heatmap(house_data_imputed.corr(), annot=True, cmap='coolwarm', linewidths=.5)
X = house_data_imputed.drop('price', axis=1)
y = house_data_imputed['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
example_input = pd.DataFrame({
    'area': [1800],
    'bedrooms': [3],
    'bathrooms': [2]
})
model = LinearRegression()
model.fit(X_train, y_train)
predicted_price = model.predict(example_input)
print("\nPredicted Price of the House:")
print(predicted_price)
