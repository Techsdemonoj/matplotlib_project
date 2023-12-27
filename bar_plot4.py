import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


children = [10,20,40,10,30]
colors = ['red red red red red red','blue blue blue blue','green green green green green','yellow yellow yellow yellow ','pink pinkpinkpink']

plt.bar(colors,children,color = 'blue')
# vertical bar chart
plt.xticks(rotation='vertical')
plt.show()