class Perceptron:
    def __init__(self, weights, inputs, learning_rate=0.1, bias=0.1):
        self.learning_rate = learning_rate
        self.bias = bias
        self.weights = weights
        self.inputs = inputs

    def step_function(self, z):
        return z
    
    def predict(self, inputs):
        weighted_sum = self.bias
        for i in range(len(self.weights)):
            weighted_sum += self.weights[i]*inputs[i]
            return self.step_function(weighted_sum)
    
    def train(self, inputs, target):
        i = 1
        while True:
            output = self.predict(inputs)
            loss = target - output
            i += 1
            print(f'Epoch {i}: Loss: {loss}, Output: {output}')
            if(abs(loss)<1e-1):
                print(f'Target reached after {i} epoches.')
                break
            for j in range(len(self.weights)):
                self.weights[j] += self.learning_rate*loss*inputs[j]

weights = [0.1, 0.3, 0.2]
inputs = [0.8,0.6,0.4]
target=0.8
perceptron = Perceptron(weights=weights, inputs=inputs)
perceptron.train(inputs, target)