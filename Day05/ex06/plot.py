import numpy as np
import matplotlib.pyplot as plt


def plot_with_loss(x, y, theta):
    for p in range(1, len(x) + 1):
        plt.plot([p, p], [y[p-1], theta[0] + theta[1] * p], 'bo', linestyle="--")
    plt.plot(x, y, 'b.')
    plt.plot([1, len(x)], [theta[0] + theta[1] * 1, theta[0] + theta[1] * len(x)])
    plt.show()
