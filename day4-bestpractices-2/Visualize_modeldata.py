import scipy
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import (MultipleLocator)
from matplotlib import pylab

model_data = np.load("I_q_IPA_model.npy")

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(model_data[:, 0], model_data[:, 1])

plt.show()