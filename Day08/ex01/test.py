import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR


lr = MyLR(np.array([[2], [0.5]]), 2.5e-5, 100000)
x = np.array([4]).reshape((-1, 1))
print(lr.logistic_predict_(x))
x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
print(lr.logistic_predict_(x2))
x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
lr2 = MyLR(np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]]), 2.5e-5, 100000)
print(lr2.logistic_predict_(x3))

