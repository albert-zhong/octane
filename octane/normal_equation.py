import numpy as np
import scipy.linalg as linalg


def normal_equation(X, y):
    theta = np.array(linalg.pinv(X.T @ X) @ X.T @ y)
    return theta
