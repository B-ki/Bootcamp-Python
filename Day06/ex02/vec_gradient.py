import numpy as np
from prediction import predict_
from tools import add_intercept


def simple_gradient(x, y, theta):
    mat_X = predict_(x, theta)
    mat_X_T = np.transpose(add_intercept(x))
    # return np.matmul(mat_X_T, np.subtract(mat_X, y)) / len(y) # same as below
    return mat_X_T @ (mat_X - y) / len(y)
