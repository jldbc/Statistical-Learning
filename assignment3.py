from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
boston = load_boston()
boston_data = pd.DataFrame(data = np.hstack([boston.target[:,np.newaxis], boston.data]), columns = ["price"] + list(boston["feature_names"]))

DIS = boston_data.ix[:, "DIS"].values[:,np.newaxis]
NOX = boston_data.ix[:, "NOX"].values[:,np.newaxis]

def create polynomial matrix(X, degree):
    mat = np.array(len(x), degree)
