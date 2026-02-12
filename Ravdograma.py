import numpy as np
import matplotlib.pyplot as plt

# Δείγμα δεδομένων
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
values_1 = [68, 74, 86, 91, 86]
values_2 = [30, 29, 21, 76, 74]

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')

xpos = np.arange(len(categories))
ypos = np.zeros(len(categories))
zpos = np.zeros(len(categories))
dx = np.ones(len(categories))
dy = np.array(values_2)
dz = np.array(values_1)

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='purple')

ax.set_xticks(xpos)
ax.set_xticklabels(categories)
ax.set_ylabel('Value 2')
ax.set_zlabel('Value 1')
plt.show()