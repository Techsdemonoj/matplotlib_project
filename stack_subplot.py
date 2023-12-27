import matplotlib.pyplot as plt

# Data
groups = ['G1', 'G2', 'G3', 'G4', 'G5']
values1 = [12, 19, 14, 27, 16]
values2 = [21, 30, 15, 17, 20]

fig, ax = plt.subplots()

# Stacked bar chart
ax.bar(groups, values1)
ax.bar(groups, values2, bottom=values1)

plt.show()

