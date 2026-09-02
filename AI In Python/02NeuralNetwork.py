import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Create a local CSV file with 150 observations
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df.to_csv('iris_data.csv', index=False)

print("File 'iris_data.csv' created successfully.")

# 2. Implement a Neural Network
# Load data from the created file
data = pd.read_csv('iris_data.csv')

X = data.drop('target', axis=1)
y = data['target']

# Split and scale data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Define MLP with two hidden layers: (5 neurons, 3 neurons)
mlp = MLPClassifier(
    hidden_layer_sizes=(5, 3),
    max_iter=1000,
    random_state=42
)

mlp.fit(X_train_scaled, y_train)

# 3. Plot the Neural Network Structure
def plot_neural_network(model):
    layers = [model.n_features_in_] + list(model.hidden_layer_sizes) + [model.n_outputs_]

    fig, ax = plt.subplots(figsize=(8, 6))

    # Calculate spacing
    v_spacing = 1.0 / (max(layers) + 1)
    h_spacing = 1.0 / (len(layers) + 1)

    for i, layer_size in enumerate(layers):
        layer_top = v_spacing * (layer_size - 1) / 2.0 + 0.5

        for j in range(layer_size):
            # Draw neuron
            circle = plt.Circle(
                ((i + 1) * h_spacing, layer_top - j * v_spacing),
                0.02,
                color='skyblue',
                ec='black',
                zorder=4
            )
            ax.add_artist(circle)

            # Connect to next layer
            if i < len(layers) - 1:
                next_layer_size = layers[i + 1]
                next_layer_top = v_spacing * (next_layer_size - 1) / 2.0 + 0.5

                for k in range(next_layer_size):
                    line = plt.Line2D(
                        [(i + 1) * h_spacing, (i + 2) * h_spacing],
                        [layer_top - j * v_spacing, next_layer_top - k * v_spacing],
                        c='gray',
                        lw=0.5,
                        alpha=0.5
                    )
                    ax.add_artist(line)

    plt.title("Iris Neural Network Architecture (4-5-3-3)")
    plt.axis('off')
    plt.show()


plot_neural_network(mlp)
