import numpy as np

def gradient_descent(X,y,lr=0.1,epochs=1000):
    m,c =0.0,0.0
    n = len(X)

    for _ in range(epochs):
        y_pred = m*X +c
        dm =(-2/n) * np.sum(X*(y - y_pred))
        dc = (-2/n)* np.sum(y-y_pred)
        m -= lr*dm
        c -= lr*dc

        return m,c
