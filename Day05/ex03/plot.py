import numpy as np
from prediction import predict_
import matplotlib.pyplot as plt


def plot(x, y, theta):
    plt.plot(x, y, 'b.')
    plt.plot([1, len(x)], [theta[0] + theta[1] * 1, theta[0] + theta[1] * len(x)])
    plt.show()
