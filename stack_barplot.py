# stacked bar plot with three subgroups

import  matplotlib.pyplot as plt
import numpy as np
groups = ['G1', 'G2', 'G3', 'G4', 'G5']
values1 = [12, 19, 14, 27, 16]
values2 = [21, 30, 15, 17, 20]
values3 = [15, 23, 12, 11, 15]

fig, ax = plt.subplots()

ax.bar(groups, values1)
ax.bar(groups, values2, bottom = values1)
ax.bar(groups, values3, bottom = np.add(values1, values2))

plt.show()