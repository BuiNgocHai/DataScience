import numpy as np
x = np.random.randint(0, 100, 20)
y = np.random.uniform(0, 20)
y
print(x)
print(y)
index = np.argmin(np.abs(np.array(x)-y))
print(" index of x where the value at that index is closest to y ",index)
print(" value at that index is closest to yin x: ",x[index])
