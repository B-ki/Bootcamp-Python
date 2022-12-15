import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR


age_lr = MyLR([[1000.0], [-1]], 2.5e-5, 100000)

x = np.array([[-4]])
print(age_lr.sigmoid(x))
x = np.array([[2]])
print(age_lr.sigmoid(x))
x = np.array([[-4], [2], [0]])
print(age_lr.sigmoid(x))
