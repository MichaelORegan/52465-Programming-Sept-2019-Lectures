import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0, 1.0, 1000)

plt.hist(x, bins = 20)

plt.show()