import matplotlib
matplotlib.use('tkagg')

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot
# plt.savefig('plot.png', edgecolor='RED', transparent=True)