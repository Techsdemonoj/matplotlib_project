import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eun_emp = pd.read_csv("D:/python & sql tutorial materials/sql practice data/unemployed_population.csv")
# eun_emp = eun_emp.head(50)
# plt.scatter(eun_emp['year'], eun_emp['advanced_degree'],color = "green",linestyle = 'dashdot',marker = '.')
# plt.plot(eun_emp['year'], eun_emp['advanced_degree'],color = "red",linestyle = 'dashed',marker = '.')
# plt.plot(eun_emp['year'], eun_emp['high_school'],color = "blue",linestyle = 'dashed',marker = '.')


plt.bar(eun_emp['year'], eun_emp['advanced_degree'], color='skyblue', edgecolor='black', linewidth=1.2)
# plt.bar(np.arange(eun_emp.shape[0]), eun_emp['advanced_degree'], color='skyblue', edgecolor='black', linewidth=1.2)

# print(eun_emp)
plt.xlabel('year')
plt.ylabel('advanced_degree')
# plt.title('Ave and sr analysis')
plt.show()



