import matplotlib.pyplot as plt
import numpy as np

xdata = [0, 1, 2, 3, 4, 5]
ydata = [0.1, 0.2, 0.4, 0.8, 0.6, 0.1]
width = [0.05, 0.1, 0.2, 0.4, 0.3, 0.05]

plt.bar(xdata, ydata, linewidth=1.0, edgecolor='k', width=width)
plt.show()
