# you can modify the border color and width of the bars with "edgecolor" and "linewidth", respectively
import matplotlib.pyplot as plt

# Data
groups = ['G1', 'G2', 'G3', 'G4', 'G5']
values1 = [12, 19, 14, 27, 16]
values2 = [21, 30, 15, 17, 20]

fig, ax = plt.subplots()

# Stacked bar chart
ax.bar(groups, values1, color = "#44a5c2",
       edgecolor = "black", linewidth = 2)
ax.bar(groups, values2, bottom = values1, color = "#ffae49",
       edgecolor = "black", linewidth = 2)

plt.show()

