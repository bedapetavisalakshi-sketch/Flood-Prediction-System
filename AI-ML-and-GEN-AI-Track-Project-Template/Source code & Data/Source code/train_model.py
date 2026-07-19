import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

# ==========================
# Load Dataset
# ==========================

data = pd.read_csv("../flood_dataset_classification.csv")


print("Dataset Preview:")
print(data.head())

print("\nOriginal Columns:")
print(data.columns)

# ==========================
# Rename Columns
# ==========================

data.rename(columns={
    "Disaster Type": "Disaster_Type",
    "Total Deaths": "Total_Deaths",
    "Total Affected": "Total_Affected"
}, inplace=True)

print("\nUpdated Columns:")
print(data.columns)

# ==========================
# Encode Disaster Type
# ==========================

encoder = LabelEncoder()
data["Disaster_Type"] = encoder.fit_transform(data["Disaster_Type"])

# ==========================
# Features and Target
# ==========================

X = data[
    [
        "Disaster_Type",
        "Latitude",
        "Longitude",
        "Total_Deaths",
        "Total_Affected",
        "duration",
        "time",
        "Rainfall",
        "Elevation",
        "Slope",
        "distance"
    ]
]

y = data["occured"]

# ==========================
# Train Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================
# Models
# ==========================

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "KNN": KNeighborsClassifier(
        n_neighbors=5
    ),

    "XGBoost": XGBClassifier(
        n_estimators=100,
        learning_rate=0.05,
        max_depth=5,
        eval_metric="logloss",
        random_state=42
    )
}

# ==========================
# Train Models
# ==========================

best_model = None
best_accuracy = 0

for name, model in models.items():

    print("\n==============================")
    print(f"Training {name}")

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print(f"Accuracy: {accuracy * 100:.2f}%")

    print(classification_report(y_test, prediction))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# ==========================
# Save Model
# ==========================

joblib.dump(best_model, "flood_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")

print("\n==============================")
print(f"Best Model Accuracy: {best_accuracy * 100:.2f}%")
print("Saved: flood_model.pkl")
print("Saved: label_encoder.pkl")
print("==============================")