import random

import numpy as np

import model
import parameterFitting
import social_units as su
import matplotlib.pyplot as plt


#total_infected = model.model()
#print(total_infected)
#parameterFitting.parameterFit()

x_real = np.array([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 28, 29, 30, 31, 34
])

y_real = np.array([
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 20, 61, 64, 70, 135, 174, 218, 285, 355, 454, 542, 621, 634,
    691
])
plt.plot(x_real, y_real, 'o')
x = np.arange(35)
y = model.model(x,0.001, 0.00016385714285714286) #0.0009388367346938776, 0.00016385714285714286
plt.plot(x, y)
plt.plot()
plt.show()
