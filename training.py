# Train and save the disease prediction model
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load and encode data
df = pd.read_csv("train_data.csv")
symptom_columns = df.columns.drop("disease")
X = df[symptom_columns].applymap(lambda x: 1 if x == 'yes' else 0) if df[symptom_columns].dtypes[0] == object else df[symptom_columns]
y = df["disease"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluate
print(classification_report(y_test, model.predict(X_test)))

# Save model
joblib.dump(model, "disease_model.pkl")
print("Model saved as disease_model.pkl")

