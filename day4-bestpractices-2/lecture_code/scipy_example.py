from scipy.optimize import minimize_scalar

f = lambda x: (x - 2) * (x + 1)**2
res = minimize_scalar(f, bounds=(-8, -5),method='bounded')
print(res)

from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(-8,-5,100)
plt.plot(x,f(x))
plt.show()

from scipy.special import j1

# Find minimum of the the Bessel function of the first kind order 1
res = minimize_scalar(j1, bounds=(4, 7), method='bounded')
print(res)

x = np.linspace(4,7,100)
plt.plot(x,j1(x))
plt.show()