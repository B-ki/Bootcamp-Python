from tools import add_intercept
import numpy as np


x = np.arange(1, 6)
print(add_intercept(x))
y = np.arange(1, 10).reshape((3, 3))
print(add_intercept(y))
