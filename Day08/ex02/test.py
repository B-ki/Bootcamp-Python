import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR


y1 = np.array([1]).reshape((-1, 1))
x1 = np.array([4]).reshape((-1, 1))
lr = MyLR(np.array([[2], [0.5]]), 2.5e-5, 100000)
y_hat1 = lr.logistic_predict_(x1)
print(lr.vec_log_loss_(y1, y_hat1))
