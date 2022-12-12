import numpy as np
from vec_loss import loss_
from other_losses import mse_, rmse_, mae_, r2_score_


X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
print(loss_(X, Y))
print(mse_(X, Y))
print(rmse_(X, Y))
print(mae_(X, Y))
print(r2_score_(X, Y))
