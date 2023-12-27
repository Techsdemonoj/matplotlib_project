import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("D:\python & sql tutorial materials\sql practice data\iris.csv")
# print(iris)

plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'])
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
# iris.sample(5)

# Create a mapping for species to numerical labels
species_mapping = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}

# Replace values in the 'Species' column
iris['Species'] = iris['Species'].replace(species_mapping)
plt.show()