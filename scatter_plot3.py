import numpy as np

import matplotlib.pyplot as plt

plt.figure(dpi=100)

# Fixing random state for reproducibility

np.random. seed(100)

n = 20

x = np.random.rand(n)

y = np.random.rand(n)

colors = np.random.rand(n)

area = (30 * np.random.rand(n))**2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)

# Add title

plt.title('Scatter plot')

plt.show()