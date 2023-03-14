import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


# -------Generate Data---------

data = np.random.normal(loc=5., scale=2., size=(10000,))

mu, sigma = norm.fit(data)
"""
Simple first plot
"""

if False:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(data, range=(-5, 15), bins=20)
    plt.show()

"""
Fit a Gaussian to the data and plot it
"""
if False:
    print(mu)
    print(sigma)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(data, range=(-5, 15), bins=1000, density=True)
    ax.plot(np.arange(-5, 15, 0.1), norm.pdf(np.arange(-5, 15, 0.1), mu, sigma), color="red")
    plt.show()

if False:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('My fancy plot')
    ax.hist(data, range=(-5, 15), bins=20, density=True, label='data', color='0.75', lw=0.2)
    ax.plot(np.arange(-5, 15, 0.1), norm.pdf(np.arange(-5, 15, 0.1), mu, sigma), label='fit', color='r')
    ax.set_xlabel(r'Some variable $\varphi$')
    ax.set_ylabel(r'Probability density')
    ax.legend(loc=1)
    plt.show()

if False:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('My fancy plot')
    ax.hist(data, range=(-5, 15), bins=20, density=True, label='data', color='0.75', lw=0.2)
    ax.plot(np.arange(-5, 15, 0.1), norm.pdf(np.arange(-5, 15, 0.1), mu, sigma), label='fit', color='r')
    ax.set_xlabel(r'Some variable $\varphi$')
    ax.legend(loc=2, frameon=False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='x', which='both', bottom='on', top='off')
    ax.tick_params(axis='y', which='both', left='off', right='off', labelleft='off')
    plt.show()

if True:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('My fancy plot')
    ax.hist(data, range=(-5, 15), bins=20, density=True, label='data', color='0.75', lw=0.2)
    ax.plot(np.arange(-5, 15, 0.1), norm.pdf(np.arange(-5, 15, 0.1), mu, sigma), label='fit', color='r')
    ax.set_xlabel(r'Some variable $\varphi$')
    ax.legend(loc=2, frameon=False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='x', which='both', bottom='on', top='off', labelright="off")
    ax.tick_params(axis='y', which='both', left='off', right='off')
    fig.savefig('my_fancy_plot.pdf', format='pdf', bbox_inches='tight')