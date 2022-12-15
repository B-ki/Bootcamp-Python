import numpy as np
import matplotlib.pyplot as plt
import math


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

    def mse_(self, y, y_hat):
        return (np.square(np.subtract(y, y_hat))).mean()

    def rmse_(self, y, y_hat):
        return math.sqrt((np.square(np.subtract(y, y_hat))).mean())

    def mae_(self, y, y_hat):
        return (np.absolute(np.subtract(y, y_hat))).mean()

    def r2_score_(self, y, y_hat):
        num = (np.square(np.subtract(y, y_hat))).sum()
        new_arr = [x - y.mean() for x in y]
        denum = (np.square(new_arr)).sum()
        return 1 - num/denum

    def plot(self, x, y):
        plt.plot(x, self.predict_(x), "--", color='C2')
        graph1 = plt.scatter(x, self.predict_(x), marker='X', color='C2')
        graph2 = plt.scatter(x, y, marker='o', color='C9')
        plt.xlabel("Quantity of blue pills (in micrograms)")
        plt.ylabel("Space driving score")
        graph1.set_label('Strue(pills)')
        graph2.set_label('Spredicted(pills)')
        plt.legend()
        plt.grid()
        plt.show()

    def plot_J(self, x, y):
        theta_org = self.thetas
        for t0 in np.arange(theta_org[0] - 2, theta_org[0] + 3, 1):
            J = []
            thetas1 = []
            for t1 in np.arange(-14, -4, 0.1):
                self.thetas = [t0, t1]
                J.append(self.loss_(y, self.predict_(x)))
                thetas1.append(t1)
            plt.plot(thetas1, J)
        plt.show()

