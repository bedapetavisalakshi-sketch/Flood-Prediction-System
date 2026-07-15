import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load dataset
data = pd.read_csv("../Dataset/flood_dataset_classification.csv")

print("Dataset Loaded")
print(data.head())


# Separate features and target

X = data.drop("occured", axis=1)
y = data["occured"]


# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Machine Learning model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train model

model.fit(X_train, y_train)


# Test model

y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Model Accuracy:", accuracy)


# Save trained model

joblib.dump(model, "flood_model.pkl")

print("flood_model.pkl created successfully")