import math
import numpy as np

class Perceptron:
    def __init__(self, weights, inputs, targets, learning_rate=0.1, bias=0.5):
        self.inputs = inputs
        self.targets = targets
        self.learning_rate = learning_rate
        self.bias = bias
        self.weights = weights
        self.outputs = [0,0]

    def step_function(self, z):
        return 1/(1+(math.e**-z))
    
    def softmax(self, x):
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum(keepdims=True)
    
    def forward(self, inputs):
        for i in range(len(self.outputs)):
            weighted_sum = self.bias
            for j in range(len(inputs)):
                weighted_sum += self.weights[i][j] * inputs[j]
            self.outputs[i] = self.step_function(weighted_sum)
        return self.outputs
    
    def train(self, inputs, targets):
            outputs = self.forward(inputs)
            print("Output: ", outputs)
            softmaxxed_output = self.softmax(outputs)
            print(f"Softmaxxed output: ", softmaxxed_output)
            losses = [targets[0] - outputs[0] ,targets[1] - outputs[1]]
            print(f'Epoch {1}: Loss: {losses}, Output: {outputs}')

weights = [[0.1,0.2,0.3,0.4],[0.5,0.6,0.7,0.8],[0.9,0.1,0.2,0.3]]
inputs = [0.3, 0.5]
targets = [0, 1]
perceptron = Perceptron(weights=weights, inputs=inputs, targets=targets)
perceptron.train(inputs, targets=targets)