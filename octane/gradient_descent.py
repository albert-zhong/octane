import numpy as np


class GradientDescent:

    theta = np.matrix([])  # Parameters

    X = np.matrix([])
    y = np.matrix([])
    m = 1  # Number of training examples
    n = 1  # Number of features

    alpha = 0.01  # Learning rate
    iterations = 100  # Number of iterations of gradient descent

    def __init__(self, X, y, alpha, iterations):
        self.X = X
        self.y = y

        self.m = X.shape[0]
        self.n = X.shape[1]

        self.alpha = alpha
        self.iterations = iterations
        self.theta = np.zeros((self.n, 1))

    def learn(self):
        for i in range(self.iterations):
            temp = np.matmul(self.X, self.theta)
            error = np.subtract(temp, self.y)
            new_X = np.matmul(error.T, self.X)
            self.theta = self.theta - np.multiply((self.alpha/self.m), new_X.T)
