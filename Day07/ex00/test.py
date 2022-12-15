import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR

x = np.arange(1,13).reshape((4,-1))
theta1 = np.array([5, 0, 0, 0]).reshape((-1, 1))
MLR = MyLR(theta1)
print(theta1)
print(MLR.predict_(x))
theta2 = np.array([0, 1, 0, 0]).reshape((-1, 1))
MLR2 = MyLR(theta2)
print(MLR2.predict_(x))
theta3 = np.array([-1.5, 0.6, 2.3, 1.98]).reshape((-1, 1))
MLR3 = MyLR(theta3)
print(MLR3.predict_(x))
theta4 = np.array([-3, 1, 2, 3.5]).reshape((-1, 1))
MLR4 = MyLR(theta4)
print(MLR4.predict_(x))
