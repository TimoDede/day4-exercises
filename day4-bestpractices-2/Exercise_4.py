from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from matplotlib.ticker import (MultipleLocator)
from matplotlib import pylab

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ------------------------------Define layout--------------------------------------------------------
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

plt.rc('font', size=16)  # controls default text sizes
plt.rc('axes', titlesize=16)  # font-size of the axes title
plt.rc('axes', labelsize=16)  # font-size of the x and y labels
plt.rc('axes', linewidth=2)  # line-thickness of axes
plt.rc('xtick', labelsize=16)  # font-size of the xtick labels
plt.rc('ytick', labelsize=16)  # font-size of the tick labels
plt.rc('legend', fontsize=16)  # font-size of legend
plt.rc('figure', titlesize=14)  # font-size of the figure title
plt.rc('lines', linewidth=2)  # line-thickness
plt.rc('lines', markersize=3)  # size of markers
pylab.rcParams['xtick.major.pad'] = '10'  # increases the distance from the ticks from the respective axis
pylab.rcParams['ytick.major.pad'] = '10'  # increases the distance form the ticks from the respective axis

exp_data = np.load("I_q_IPA_exp.npy")
theoretical_data = np.load("I_q_IPA_model.npy")

# interpolate Theoretical Data
inter = interpolate.interp1d(theoretical_data[:, 0], theoretical_data[:, 1])
x_theo_interpolated = np.arange(0, theoretical_data[-1, 0], 0.1)

scaled_model_data = theoretical_data[:, 1]
y_theo_interpolated = inter(exp_data[:, 0])  # use interpolation function returned by `interp1d`


def f(x):
    y = x * y_theo_interpolated/exp_data[:, 1]
    return y


res = minimize_scalar(f)
print(res.x)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(exp_data[:, 0], exp_data[:, 1], 'o', label="Exp Data", color="blue")
# plt.plot(xnew, ynew, "--", label="Theory", color="black")
plt.plot(theoretical_data[:, 0], theoretical_data[:, 1] / 10000, marker="o", label="Rescaled Theo. Data", color="red")
# plt.plot(x_theo_interpolated, y_theo_interpolated/10000, label="Rescaled Theo. Data", color="red")


ax.set_xlabel(r'Scattering Strength')
ax.set_ylabel(r'Scattering Vector')
plt.legend(loc="upper right", frameon=False, labelspacing=0.4,
           labelcolor='linecolor', handletextpad=1.0, handlelength=0.0)

# +++++++++++Define data range to be shown+++++++++++

# plt.ylim(5, 40)
# plt.xlim(0, 18)

# ++++++++++++Define tick parameters++++++++++++++++++++++++++++++

plt.tick_params(which="major", direction='in', length=8, width=2, bottom=True, top=True, left=True, right=True)
plt.tick_params(which="minor", direction='in', length=4, width=2, bottom=True, top=True, left=True, right=True)

# ++++++++++++Locate major and minor ticks+++++++++++++++++++++++

# X-AXIS
# ax.xaxis.set_major_locator(MultipleLocator(4))
# ax.xaxis.set_minor_locator(MultipleLocator(2))

# Y-AXIS
# ax.yaxis.set_major_locator(MultipleLocator(5))
# ax.yaxis.set_minor_locator(MultipleLocator(2.5))
# Define labels of ticks
plt.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False)

plt.show()
