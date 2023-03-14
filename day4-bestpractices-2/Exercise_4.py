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

#Load Data
exp_data = np.load("I_q_IPA_exp.npy")
theoretical_data = np.load("I_q_IPA_model.npy")

# interpolate Theoretical Data
func_theory_interpolated = interpolate.interp1d(theoretical_data[:, 0], theoretical_data[:, 1])
theoretical_data_interpolated = func_theory_interpolated(exp_data[:, 0])

# Define a function for the mean square displacement
def scaling_f(x):
    return np.nansum((exp_data[:, 1] - x * theoretical_data_interpolated)**2)

# Find the scaling factor
scaling_factor = minimize_scalar(scaling_f)
print(scaling_factor)

# Rescale theoretical data
theoretical_data_rescaled = theoretical_data_interpolated*(scaling_factor.x)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(exp_data[:, 0], exp_data[:, 1], 'o', label="Exp. Data", color="blue")
plt.plot(exp_data[:, 0], theoretical_data_rescaled, ls="-", label="Rescaled Theo. Data", color="blue", alpha=0.4 )


ax.set_xlabel(r'Scattering Strength')
ax.set_ylabel(r'Scattering Vector')
plt.legend(loc="upper left")

# +++++++++++Define data range to be shown+++++++++++

# plt.ylim(5, 40)
plt.xlim(0, 18.5)

# ++++++++++++Define tick parameters++++++++++++++++++++++++++++++

plt.tick_params(which="major", direction='in', length=8, width=2, bottom=True, top=True, left=True, right=True)
plt.tick_params(which="minor", direction='in', length=4, width=2, bottom=True, top=True, left=True, right=True)

# ++++++++++++Locate major and minor ticks+++++++++++++++++++++++

# X-AXIS
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(2.5))

# Y-AXIS
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_minor_locator(MultipleLocator(5))

# Define labels of ticks
plt.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False)

plt.show()
