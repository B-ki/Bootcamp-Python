import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR

theta1 = np.array([5, 0, 0, 0]).reshape((-1, 1))
MLR = MyLR(theta1)
X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((-1, 1))
Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))

print(MLR.loss_(X, Y))
print(MLR.loss_(X, X))
