import numpy as np


def loss_(y, y_hat):
    return (np.square(np.subtract(y, y_hat))).mean()/2
