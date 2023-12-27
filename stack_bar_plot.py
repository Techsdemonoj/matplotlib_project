import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# taking data from a csv file
df = pd.read_csv("D:/python & sql tutorial materials/sql practice data/batsman_season_record.csv")
plt.bar(df['batsman'], df['2015'], color='skyblue')
plt.bar(df['batsman'], df['2016'], color='blue', bottom=2015)
plt.bar(df['batsman'], df['2017'], color='green', bottom=2015+2016)
plt.show()
