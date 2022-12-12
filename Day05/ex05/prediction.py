import numpy as np
from tools import add_intercept


def predict_(x, theta):
    return np.matmul(add_intercept(x), theta)
