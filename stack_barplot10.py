# stacked bar chart
import numpy as np
import pandas as np
import matplotlib .pyplot as plt
import pandas as pd

df = pd.read_csv("D:/python & sql tutorial materials/sql practice data/batsman_season_record.csv")
# print(df)

plt.bar(df['batsman'], df['2017'], label='2017')
plt.bar(df['batsman'], df['2016'], bottom=df['2017'], label='2016')
plt.bar(df['batsman'], df['2015'], bottom=(df['2016'] + df['2017']), label='2015')
plt.legend()
plt.show()
