import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    'Occupation': ['Engineer', 'Doctor', 'Teacher', 'Doctor', 'Engineer'],
    'Credit_Score': [700, 800, 650, None, 720]
}
df = pd.DataFrame(data)
print("First five rows:")
print(df.head())
print("\nBasic statistical computations:")
print(df.describe())
print("\nColumns and their data types:")
print(df.dtypes)
df['Credit_Score'].fillna(df['Credit_Score'].mode()[0], inplace=True)
print("\nAfter handling null values:")
print(df)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Occupation', y='Credit_Score', data=df)
plt.title('Credit Scores Based on Occupation')
plt.show()
X_train, X_test, y_train, y_test = train_test_split(df[['Occupation']], df['Credit_Score'], test_size=0.2, random_state=42)
numeric_features = []  
categorical_features = ['Occupation']
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('classifier', GaussianNB())])
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("\nPredictions:", predictions)
