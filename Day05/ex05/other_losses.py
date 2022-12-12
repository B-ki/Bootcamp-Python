import numpy as np
import math


def mse_(y, y_hat):
    return (np.square(np.subtract(y, y_hat))).mean()


def rmse_(y, y_hat):
    return math.sqrt((np.square(np.subtract(y, y_hat))).mean())


def mae_(y, y_hat):
    return (np.absolute(np.subtract(y, y_hat))).mean()


def r2_score_(y, y_hat):
    num = (np.square(np.subtract(y, y_hat))).sum()
    new_arr = [x - y.mean() for x in y]
    denum = (np.square(new_arr)).sum()
    return 1 - num/denum
