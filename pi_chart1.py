# pi_chart used for
# Uni variate vs numerical
# use case- to find contribution on a standard scale

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [23, 45, 100, 20, 49]
subjects = ['eng', 'science', 'maths', 'sst', 'hindi']

# use pi package for getting pi chart
plt.pie(data)


# getting name for all pi chart
# plt.pie(data, labels=subjects)

plt.show()
