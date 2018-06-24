import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['lines.linewidth']
mpl.rcParams['lines.color'] = 'r'

mpl.rc('lines', linewidth=2, color='r')

t = np.arange(0.0, 1.0, 0.01)

s = np.sin(2 * np.pi * t)

plt.rcParams['lines.color'] = 'r'
plt.plot(t,s)

c = np.cos(2 * np.pi * t)

plt.rcParams['lines.linewidth'] = '3'
plt.plot(t,c)

plt.show()