# The color of the bars for each subgroup can be customized through the color argument.
# Note that you can also customize the transparency of the colors with "alpha"
import matplotlib.pyplot as plt
# data
groups = ['G1', 'G2', 'G3', 'G4', 'G5']
values1 = [12, 19, 14, 27, 16]
values2 = [21, 30, 15, 17, 20]
fig, ax = plt.subplots()

# stacked bar chart

ax.bar(groups, values1, color = "#024b7a", alpha = 0.5)
ax.bar(groups, values2, bottom = values1, color = "#44a5c2", alpha = 0.5)

plt.show()
