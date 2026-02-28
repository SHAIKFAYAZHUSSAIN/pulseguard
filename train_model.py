import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Load dataset
df = pd.read_csv("your_dataset.csv")  # replace with your file name

# Select features
X = df[['Age', 'SystolicBP', 'DiastolicBP', 'Blood glucose', 'BodyTemp', 'HeartRate']]
y = df['RiskLevel']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Feature Importance
importances = model.feature_importances_
for feature, importance in zip(X.columns, importances):
    print(f"{feature}: {importance:.4f}")

# Save model
joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")