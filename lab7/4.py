import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi,np.pi, 100)

plt.plot(x, np.sin(x))
plt.plot(x, 2*np.sin(x))
plt.plot(x, 2+np.sin(x))
plt.plot(x, np.sin(2*x))
plt.show()