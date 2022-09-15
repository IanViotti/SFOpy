'''
Implements benchmark single objetctive functions
'''

import numpy as np

def poly(X):
    for d in range(np.shape(X)[1]):
        y = X[:, d]**2
    return y