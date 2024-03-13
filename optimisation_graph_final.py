import numpy as np
import matplotlib.pyplot as plt

r_range = np.linspace(0.5,49.5,1000)
array = np.genfromtxt("optimisation.txt")

plt.plot(r_range, array)
plt.xlabel('Starting radius')
plt.ylabel('Time')
plt.title('Optimisation')
plt.legend()
plt.grid(True)
#plt.plot([0.7233,0.7233], [0,max(array)], 'r-')
#plt.annotate("Venus", )
plt.xscale("log")
plt.yscale("log")
plt.show()