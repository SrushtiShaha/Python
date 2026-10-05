import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv(r"D:\AI Vighnesh Kadam\cereal.csv")

# Select features
features = [
    'calories',
    'protein',
    'fat',
    'sodium',
    'fiber',
    'carbo',
    'sugars',
    'potass'
]

X = df[features]
y = df['rating']

# Replace missing values
X = X.replace(-1, X.mean())

# Scaling
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()

X_scaled = scaler_x.fit_transform(X)
y_scaled = scaler_y.fit_transform(
    y.values.reshape(-1, 1)
).flatten()

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y_scaled,
    test_size=0.3,
    random_state=123
)

# Build model
nn_model = MLPRegressor(
    hidden_layer_sizes=(3,),
    activation='logistic',
    solver='lbfgs',
    max_iter=1000,
    random_state=123
)

# Train
nn_model.fit(X_train, y_train)

# Predict
y_pred_scaled = nn_model.predict(X_test)

# Reverse scaling
y_pred = scaler_y.inverse_transform(
    y_pred_scaled.reshape(-1, 1)
)

y_actual = scaler_y.inverse_transform(
    y_test.reshape(-1, 1)
)

# RMSE
rmse = np.sqrt(mean_squared_error(y_actual, y_pred))

print(f"Root Mean Square Error (RMSE): {rmse:.4f}")