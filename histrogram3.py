# bins handling
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:/python & sql tutorial materials/sql practice data/vk.csv")
# print(df)

plt.hist(df['batsman_runs'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
plt.show()

