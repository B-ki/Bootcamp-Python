import numpy as np
from vec_gradient import simple_gradient


def fit_(x, y, theta, alpha, max_iter):
    for i in range(0, max_iter):
        theta -= alpha * simple_gradient(x, y, theta)
    return theta
