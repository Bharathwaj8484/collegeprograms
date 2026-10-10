from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Sample mobile dataset (for demonstration purposes)
# You should replace this with a more extensive and relevant dataset
mobile_features = [
    [5.5, 32, 3, 13],
    [6.0, 64, 4, 15],
    [4.7, 16, 2, 10],
    [5.2, 32, 3, 12],
    [6.1, 128, 4, 16],
    [4.5, 16, 2, 9],
]

# Introduce more random noise to the labels
np.random.seed(42)
mobile_labels = np.array([1, 2, 1, 1, 3, 1])  # Assuming 1, 2, and 3 represent different price ranges
noise_mask = np.random.choice([True, False], size=len(mobile_labels), p=[0.7, 0.3])
mobile_labels[noise_mask] = np.random.randint(1, 4, size=np.sum(noise_mask))

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(mobile_features, mobile_labels, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree classifier
decision_tree_classifier = DecisionTreeClassifier()
decision_tree_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = decision_tree_classifier.predict(X_test)

# Display accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Example: Predict the price range for a new mobile
new_mobile_features = [[5.8, 64, 3, 14]]
predicted_price_range = decision_tree_classifier.predict(new_mobile_features)
print(f"Predicted Price Range for the New Mobile: {predicted_price_range[0]}")
