import numpy as np
import matplotlib.pyplot as plt

# Δείγμα δεδομένων
x = np.linspace(0, 100, 100)
y = np.linspace(0, 50, 50)
x, y = np.meshgrid(x, y)
z = np.sin(0.1 * x) * np.cos(0.1 * y)

fig = plt.figure(figsize=(24, 12))
ax = fig.add_subplot(111, projection="3d")

# η cmap ορίζει το χρωματικό χάρτη, ενώ η edgecolor ορίζει το χρώμα των ακμών μεταξύ των πολυγώνων της επιφάνειας
ax.plot_surface(x, y, z, cmap="viridis", edgecolor="none")

ax.set_xlabel("Field Length (m)")
ax.set_ylabel("Field Width (m)")
ax.set_zlabel("Elevation (m)")
ax.view_init(elev=25, azim=-60)
plt.show()