import numpy as np

def generate_data(seed=0,n_samples=100):
    np.random.seed(seed)
    X = 2* np.random.rand(n_samples,1)
    y = 4+3*X +np.random.randn(n_samples,1)
    return X,y