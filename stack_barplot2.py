# generalization with multiple subgropus
import matplotlib.pyplot as plt
import numpy as np
groups = ['G1', 'G2', 'G3', 'G4', 'G5']

values = np.array([[12, 19, 14, 27, 16],
                   [21, 30, 15, 17, 20],
                   [15, 23, 12, 11, 15],
                   [2, 5, 1, 6, 8]])

fig, ax = plt.subplots()

for i in range(values.shape[0]):
    ax.bar(groups, values[i], bottom=np.sum(values[:i], axis=0))


plt.show()







