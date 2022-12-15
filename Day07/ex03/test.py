import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR

x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta = np.array([[42.], [1.], [1.], [1.]])
MLR = MyLR(theta, 0.0005, 42000)
theta2 = MLR.fit_(x, y)
print(theta2)
MLR2 = MyLR(theta2)
print(MLR2.predict_(x))
