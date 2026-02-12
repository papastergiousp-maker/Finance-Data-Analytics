import numpy as np
import matplotlib.pyplot as plt

# Δείγμα δεδομένων
t = np.linspace(0, 10, 100)
x = np.sin(t)
y = np.cos(t)
z = t

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()