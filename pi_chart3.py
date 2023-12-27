import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("D:/python & sql tutorial materials/sql practice data/gayle-175.csv")
print(df)

# plt.pie(df['batsman_runs'], labels=df['batsman'])


# for getting percentage in each pie chart section
plt.pie(df['batsman_runs'], labels=df['batsman'], autopct='%0.1f%%', explode=[0.3, 0, 0, 0, 0, 0.2], shadow=True)

plt.show()

