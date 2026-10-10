import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
data = {
    'Sales': [200, 300, 400, 500, 600],
    'AdvertisingExpenditure': [50, 80, 120, 150, 200]
}
sales_data = pd.DataFrame(data)
print("First five rows of the data:")
print(sales_data.head())
print("\nBasic statistical computations:")
print(sales_data.describe())
print("\nColumns and their data types:")
print(sales_data.dtypes)
plt.scatter(sales_data['AdvertisingExpenditure'], sales_data['Sales'])
plt.title('Scatter Plot of Sales vs Advertising Expenditure')
plt.xlabel('Advertising Expenditure')
plt.ylabel('Sales')
plt.show()
if sales_data.isnull().values.any():
    print("\nNull values detected. Replacing with mode value.")
    sales_data.fillna(sales_data.mode().iloc[0], inplace=True)
X = sales_data[['AdvertisingExpenditure']]
y = sales_data['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error: {mse}")
new_advertising_expenditure = [[250]]  
predicted_sales = model.predict(new_advertising_expenditure)
print(f"\nPredicted Sales for the Next Quarter: {predicted_sales[0]}")
