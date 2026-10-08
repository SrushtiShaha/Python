import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
df = pd.read_csv(
    r"D:\AI Vighnesh Kadam\dividendinfo.csv"
)

# Features and target
X = df.drop('dividend_pays', axis=1)
y = df['dividend_pays']

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.3,
    random_state=42
)

# Model
nn_model = MLPClassifier(
    hidden_layer_sizes=(10, 5),
    activation='logistic',
    max_iter=1000,
    random_state=42
)

# Train
nn_model.fit(X_train, y_train)

# Predict
predictions = nn_model.predict(X_test)

# Results
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))