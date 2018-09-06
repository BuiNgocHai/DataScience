import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)