import numpy as np
import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values_set1 = [25, 40, 30, 35]
values_set2 = [30, 35, 25, 40]

# Set the width of the bars
bar_width = 0.35

# Create an array of indices for each category
indices = np.arange(len(categories))

# Create bar plots for each set of values
plt.bar(indices, values_set1, bar_width, label='Set 1', color='skyblue')
plt.bar(indices + bar_width, values_set2, bar_width, label='Set 2', color='orange')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Complex Bar Plot Example')

# Add legend
plt.legend()

# Customize x-axis ticks
plt.xticks(indices + bar_width / 2, categories)

# Display the plot
plt.show()
