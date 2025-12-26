#Three lines to make our compiler able to draw:
#For enqueue data-set
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([20, 40, 60, 80, 100])
ypoints = np.array([6926763000, 11475398000, 21818849000, 36104968000, 54283928000])

xpoints1 = np.array([20, 40, 60, 80, 100])
ypoints1 = np.array([4043224000, 6294735000, 11294180000, 16421561000, 25363332000])

xpoints2 = np.array([20, 40, 60, 80, 100])
ypoints2 = np.array([4113956000, 6583540000, 14927903000, 24397957000, 37142611000])





plt.plot(xpoints, ypoints, label="Array")
plt.plot(xpoints1, ypoints1, label="Unsorted")
plt.plot(xpoints2, ypoints2, label="Sorted")


leg = plt.legend(loc='upper center')
plt.title("Enqueue Operation")

plt.xlabel("Number of elements")
plt.ylabel("Time")
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
