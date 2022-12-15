import numpy as np


def add_intercept(x):
    # if not isinstance(x.any(), np.ndarray) or not x:
    #    return none
    return np.c_[np.ones(len(x)), x]
