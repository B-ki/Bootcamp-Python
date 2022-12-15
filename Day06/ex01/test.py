import numpy as np
from vec_gradient import simple_gradient
from fit import fit_
from prediction import predict_


x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
theta = np.array([1.0, 1.0]).reshape((-1, 1))
theta1 = fit_(x, y, theta, alpha=5e-8, max_iter=1500000)
print(theta1)
print(predict_(x, theta1))
