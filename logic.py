# ---------------- OR Gate ----------------
import numpy as np

# Defining the activation function
def activation_function(y):
    if y >= 0:
        return 1
    else:
        return 0

# W = weights of the perceptron model
W = np.array([1, 1])
# b = bias of the model
b = -0.5  # Adjusted bias for OR gate

# Defining the perceptron algorithm
def perceptron_algorithm(x):
    # y = w1x1 + w2x2 + b
    y = np.dot(W, x) + b
    # Apply activation function
    y = activation_function(y)
    return y

# Input values to verify the OR logic
input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

# Printing the results
print('OR Logic: \n')
print(f'x1 = 0 and x2 = 0 => y = {perceptron_algorithm(input1)}')
print(f'x1 = 0 and x2 = 1 => y = {perceptron_algorithm(input2)}')
print(f'x1 = 1 and x2 = 0 => y = {perceptron_algorithm(input3)}')
print(f'x1 = 1 and x2 = 1 => y = {perceptron_algorithm(input4)}')


# ---------------- AND Gate ----------------
import numpy as np

# Define Unit Step Function
def unitStep(v):
    if v >= 0:
        return 1
    else:
        return 0

# Perceptron Model
def perceptronModel(x, w, b):
    v = np.dot(w, x) + b
    y = unitStep(v)
    return y

# AND Logic Function
# w1 = 1, w2 = 1, b = -1.5
def AND_logicFunction(x):
    w = np.array([1, 1])
    b = -1.5
    return perceptronModel(x, w, b)

# Testing the Perceptron Model
test1 = np.array([0, 1])
test2 = np.array([1, 1])
test3 = np.array([0, 0])
test4 = np.array([1, 0])

print("\nAND Logic: \n")
print("AND({}, {}) = {}".format(0, 1, AND_logicFunction(test1)))
print("AND({}, {}) = {}".format(1, 1, AND_logicFunction(test2)))
print("AND({}, {}) = {}".format(0, 0, AND_logicFunction(test3)))
print("AND({}, {}) = {}".format(1, 0, AND_logicFunction(test4)))


# ---------------- NOR Gate ----------------
import numpy as np

# Defining the activation function (threshold at 0)
def activation_function(y):
    return 1 if y > 0 else 0

# W = weights of the perceptron model
W = np.array([-1, -1])
# b = bias of the model
b = 1.5  # Adjusted to make it work like a NOR gate

# Defining the perceptron algorithm
def perceptron_algorithm(x):
    y = np.dot(W, x) + b
    return activation_function(y)

# Input values to verify the NOR logic
inputs = [np.array([0, 0]), np.array([0, 1]), np.array([1, 0]), np.array([1, 1])]

# Printing the results
print('\nNOR Logic: \n')
for inp in inputs:
    print(f'x1 = {inp[0]} and x2 = {inp[1]} => y = {perceptron_algorithm(inp)}')

