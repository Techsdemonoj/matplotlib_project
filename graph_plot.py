import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('D:/python & sql tutorial materials/sql practice data/sharma-kohli.csv')
# print(data)
plt.plot(data['index'], data['V Kohli'],color = "green",linestyle = 'dashdot',marker = '.',label = 'virat')
plt.plot(data['index'], data['RG Sharma'],color = "red",linestyle = 'dashed',marker = '.',label = 'sharma')

plt.xlabel('YEAR')
plt.ylabel('RUN')
plt.title('RUN over the YEAR')
plt.legend()
plt.show()

