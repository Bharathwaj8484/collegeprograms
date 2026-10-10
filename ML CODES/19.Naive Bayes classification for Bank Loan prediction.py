from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
loan_features = [
    [25, 50000, 1],  
    [35, 80000, 2],
    [45, 120000, 3],
    [30, 60000, 1],
    [40, 100000, 2],
]
loan_labels = [0, 1, 1, 0, 1]  
X_train, X_test, y_train, y_test = train_test_split(loan_features, loan_labels, test_size=0.2, random_state=42)
naive = GaussianNB()
naive.fit(X_train, y_train)
y_pred = naive.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
