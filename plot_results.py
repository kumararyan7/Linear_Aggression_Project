import matplotlib.pyplot as plt 

def plot_regression(X,y,m,c):
    plt.scatter(X,y,color="blue",label="Data")
    plt.plot (X,m*X+c, color ="red",label="Regression line")
    plt.legend()
    plt.show()

