import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0
noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x, y + noise, 'r.', label='Actual') #label for legend
plt.plot(x, y, 'b-', label='Model') #label for legend

plt.title("Simple Plot")
plt.xlabel("Weight")
plt.ylabel("Mass")
plt.legend() #link to labels above

plt.show()