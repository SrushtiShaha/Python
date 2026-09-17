# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:34:58 2026

@author: mbalab
"""

import numpy as np


# Sigmoid activation and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# Dataset
# Inputs: (0,0,1), (1,1,1), (1,0,1), (0,1,1)
X = np.array([
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
])

# Corresponding Outputs
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Initialize weights randomly with mean 0
np.random.seed(1)
weights = 2 * np.random.random((3, 1)) - 1

# Training loop (Backpropagation)
for iteration in range(10000):
    # Feed Forward
    input_layer = X
    outputs = sigmoid(np.dot(input_layer, weights))

    # Calculate Error
    error = y - outputs

    # Backpropagation (Gradient Descent)
    adjustments = error * sigmoid_derivative(outputs)
    weights += np.dot(input_layer.T, adjustments)


# Predict for New Situation: (1, 0, 0)
new_situation = np.array([1, 0, 0])
prediction = sigmoid(np.dot(new_situation, weights))

print("Weights after training:")
print(weights)

print("Prediction for (1, 0, 0):", prediction[0])