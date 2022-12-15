import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR


data = pd.read_csv("../spacecraft_data.csv")
Xage = np.array(data['Age']).reshape(-1, 1)
Xthrust = np.array(data['Thrust_power']).reshape(-1, 1)
Xtera = np.array(data['Terameters']).reshape(-1, 1)
Yprice = np.array(data['Sell_price']).reshape(-1, 1)

age_lr = MyLR([[1000.0], [-1]], 2.5e-5, 100000)
# age_lr.fit_(Xage, Yprice)
Y_model_age = age_lr.predict_(Xage)
print(age_lr.thetas)
# age_lr.plot(Xage, Yprice, "age (in years)", "sell price (in keuros)", "Predicted sell price", "Sell price")

thrust_lr = MyLR([[95], [3]], 2.5e-5, 1000000)
# thrust_lr.fit_(Xthrust, Yprice)
Y_model_thrust = thrust_lr.predict_(Xthrust)
print(thrust_lr.thetas)
# thrust_lr.plot(Xthrust, Yprice, "thrust power (in 10 km/s)", "sell price (in keuros)", "Predicted sell price", "Sell price")

tera_lr = MyLR([[780.0], [-1.8]], 2.5e-5, 1000000)
# tera_lr.fit_(Xtera, Yprice)
Y_model_tera = tera_lr.predict_(Xtera)
print(tera_lr.thetas)
# tera_lr.plot(Xtera, Yprice, "distance totalizer value of spacecraft (in Tmeters)", "sell price (in keuros)", "Predicted sell price", "Sell price")

X = np.array(data[['Age', 'Thrust_power', 'Terameters']])
Y = np.array(data[['Sell_price']])

multi_lr = MyLR(np.array([[1.0], [1.0], [1.0], [1.0]]), 1e-6, 6000000)
multi_lr.fit_(X, Y)
multi_lr.plot_multi(X, Xage, Yprice, "age (in years)", "sell price (in keuros)", "Predicted sell price", "Sell price")


