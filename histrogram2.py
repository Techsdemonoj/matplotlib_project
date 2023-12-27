import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [32, 45, 56, 10, 15, 27, 61]

# bins created by given value bins= [10, 25, 40, 55, 70]
plt.hist(data,bins= [10, 25, 40, 55, 70])

plt.show()