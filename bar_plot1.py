import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# taking data from a csv file
df = pd.read_csv("D:/python & sql tutorial materials/sql practice data/batsman_season_record.csv")

print(df)
# making  plot bar side by side bar_chart (without in bar x axis we get player name)
plt.bar(np.arange(df.shape[0])-0.2,df['2015'],width = 0.2, color = 'yellow')
plt.bar(np.arange(df.shape[0]),df['2016'],width=0.2,color='red')
plt.bar(np.arange(df.shape[0])+0.2,df['2017'],width = 0.2, color = 'blue')

# in bar x axis we get player name
plt.xticks(np.arange(df.shape[0]), df['batsman'])

plt.show()