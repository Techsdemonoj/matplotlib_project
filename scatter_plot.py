import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,50)
y= 10*x +3+np.random.randint(0,300,50)

plt.scatter(x,y)
plt.plot(x,y,marker = '.')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Y = 10X + 3 + Random Noise')
plt.show()