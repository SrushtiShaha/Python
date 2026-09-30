from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# 1. Load Dataset
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split into Training (70%) and Testing (30%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=123
)

# 3. Standardise features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Train Neural Network
iris_model = MLPClassifier(
    hidden_layer_sizes=(5,),
    max_iter=200,
    solver='lbfgs',
    random_state=123
)

iris_model.fit(X_train, y_train)

# 5. Predict and Evaluate
predictions = iris_model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)

print("Confusion Matrix:")
print(cm)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")