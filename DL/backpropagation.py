import numpy as np

class Layer:
    def __init__(self, n_neurons, n_inputs, weights):
        self.learning_rate = 1
        self.weights = np.array(weights)
        self.biases = [0] * n_neurons
        self.outputs = None
        self.inputs = None
        self.deltas = None

    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.dot(inputs, self.weights.T) + self.biases
        return self.output
    
    def activation_function(self, z):
        return 1/(1+(np.e**-z))
    
    def activation_derivative(self, z):
        sigma = self.activation_function(z)
        return sigma * (1 - sigma)
    
class Network:
    def __init__(self, layers, target):
        self.target = target
        self.layers = layers

inputs = [0.35, 0.9]
layer01 = Layer(n_inputs= 2, n_neurons=2, weights=[[0.1, 0.8], [0.4, 0.6]])
layer02 = Layer(n_inputs= 2, n_neurons=1, weights=[[0.3, 0.9]])

output_layer01 = layer01.forward(inputs)
output_layer01_sigmoid = layer01.activation_function(output_layer01)

print(output_layer01)
print(output_layer01_sigmoid)

output_layer02 = layer02.forward(output_layer01_sigmoid)
output_layer02_sigmoid = layer02.activation_function(output_layer02)

print(output_layer02)
print(output_layer02_sigmoid)

target = 0.5
network = Network(layers=[layer01, layer02], target=target)

loss = target - output_layer02_sigmoid
print(f"Loss after 1 epoch: ", loss)

i = 1
while abs(loss) > 0.01:
    i += 1
    output_layer02_z = output_layer02
    output_layer02_delta = loss * layer02.activation_derivative(output_layer02_z)

    layer02.deltas = output_layer02_delta
    layer02.weights += layer02.learning_rate * loss * output_layer02_sigmoid # will change this later

    output_layer01_delta = np.dot(output_layer02_delta, layer02.weights) * layer01.activation_derivative(output_layer01)

    layer01.deltas = output_layer01_delta
    layer01.weights += layer01.learning_rate * loss * output_layer01_sigmoid

    output_layer01 = layer01.forward(inputs)
    output_layer01_sigmoid = layer01.activation_function(output_layer01)

    print(output_layer01)
    print(output_layer01_sigmoid)

    output_layer02 = layer02.forward(output_layer01_sigmoid)
    output_layer02_sigmoid = layer02.activation_function(output_layer02)

    print(output_layer02)
    print(output_layer02_sigmoid)
    loss = target - output_layer02_sigmoid
    print(f"Loss after {i} epoches: ", loss)