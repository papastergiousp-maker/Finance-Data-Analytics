import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Σημεία δεδομένων
data = {'A': (30, 9, 35), 'B': (29, 3, 33), 'C': (41, 7, 29)}

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')

# Δημιουργήστε τρισδιάστατο διάγραμμα διασποράς
for point, (x, y, z) in data.items():
    ax.scatter(x, y, z, label=point)
    ax.text(x, y, z, point)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot with Annotations')
ax.legend()
plt.show()