import numpy as np
import matplotlib.pyplot as plt

# Δείγμα δεδομένων
x = np.linspace(0, 100, 100)
y = np.linspace(0, 50, 50)
x, y = np.meshgrid(x, y)
z = np.sin(0.1 * x) * np.cos(0.1 * y)

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection="3d")

ax.plot_wireframe(x, y, z, cmap="viridis", alpha=0.8)

ax.set_xlabel("Field Length (m)")
ax.set_ylabel("Field Width (m)")
ax.set_zlabel("Elevation (m)")
ax.view_init(elev=25, azim=-60)
plt.tight_layout()
plt.show()