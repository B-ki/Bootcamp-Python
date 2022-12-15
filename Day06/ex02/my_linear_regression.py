import numpy as np


class MyLinearRegression():
    """
    Description:
        My personnal linear regression class to fit like a boss.
    """
    def __init__(self, thetas, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    def predict_(self, x):
        return np.c_[np.ones(len(x)), x] @ self.thetas

    def simple_gradient(self, x, y):
        mat_X = self.predict_(x)
        mat_X_T = np.transpose(np.c_[np.ones(len(x)), x])
        return mat_X_T @ (mat_X - y) / len(y)

    def fit_(self, x, y):
        for i in range(0, self.max_iter):
            self.thetas -= self.alpha * self.simple_gradient(x, y)
        return self.thetas

    def loss_(self, y, y_hat):
        return ((y - y_hat)**2).mean()/2

    def loss_elem_(self, y, y_hat):
        return ((y - y_hat)**2)
