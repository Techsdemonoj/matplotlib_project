# error bars
import matplotlib.pyplot as plt

# data
groups = ['G1', 'G2', 'G3', 'G4', 'G5']
values1 = [12, 19, 14, 27, 16]
values2 = [21, 30, 15, 17, 20]
values1_std = [2, 1, 3, 0.5, 2]
values2_std = [1, 4, 0.25, 0.75, 1]

fig, ax = plt.subplots()
# stacked bar chart
ax.bar(groups, values1, yerr=values1_std, ecolor='red')
ax.bar(groups, values2, yerr=values2_std, ecolor='green', bottom=values1)

plt.show()






