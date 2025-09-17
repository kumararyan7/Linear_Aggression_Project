from data_generator import generate_data
from gradient_descent import gradient_descent
from plot_results import plot_regression

#step:1 Generate data
X,y= generate_data()

#step2 : Train Model 
m,c = gradient_descent(X,y)
print (f"Final Slope:{m},intercept :{c}")

#step 3:Plot Results 
plot_regression(X,y,m,c)  