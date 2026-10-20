
import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Input data (XOR gate)
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]

# Weights and biases
w1 = [[-10, -10], [10, 10]]
b1 = [5, -5]
w2 = [10, 10]
b2 = -15

# Feed forward neural network
def predict(inputs):
    hidden = []
    for i in range(2):
        total = sum(inputs[j] * w1[i][j] for j in range(2))
        hidden.append(sigmoid(total + b1[i]))

    output = sigmoid(sum(hidden[i] * w2[i] for i in range(2)) + b2)
    return round(output)

# Display results
print("Input\tOutput")
for inputs in X:
    print(inputs, "\t", predict(inputs))
