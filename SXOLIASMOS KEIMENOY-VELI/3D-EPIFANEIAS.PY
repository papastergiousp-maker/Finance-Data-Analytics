import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Συντεταγμένες
x = np.linspace(0, 105, 100)
y = np.linspace(0, 68, 100)
x, y = np.meshgrid(x, y)

# Συνάρτηση για το διάγραμμα
z = np.sin(np.sqrt(x**2 + y**2))

# Δημιουργήστε τρισδιάστατο διάγραμμα επιφάνειας
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, cmap='viridis')

# Σημειώστε συγκεκριμένο σημείο
ax.text(52, 34, 0, 'Point of Interest', color='red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot with Annotation')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()