class HebbRule:
    def __init__(self, dataset, outputs):
        self.dataset = dataset
        self.outputs = outputs
        self.weights = [0 for data in dataset[0]]
        self.bias = 0

    def train(self):
        for data, output in zip(self.dataset, self.outputs):

            for field_index in range(len(self.weights)):

                self.weights[field_index] = self.weights[field_index] + \
                    (data[field_index] * output)

            self.bias = self.bias + output

    def get_info(self, printing=True):
        if printing:
            print("weights :", self.weights, "\nb :", self.bias)
        return self.weights, self.bias

    def test(self):
        for data, output in zip(self.dataset, self.outputs):
            sum = 0
            for field_index in range(len(self.weights)):
                sum = sum + (data[field_index] * self.weights[field_index])
            sum = sum + self.bias

            if sum >= 0:
                print(1 == output)
            else:
                print(-1 == output)
