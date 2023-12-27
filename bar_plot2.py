import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 40, 30, 45]

# Create a bar plot with customizations
plt.bar(categories, values, color='skyblue', edgecolor='black', linewidth=1.2)

# Adding labels and title
plt.xlabel('Categories', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.title('Bar Plot Example', fontsize=14)

# Adding grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
