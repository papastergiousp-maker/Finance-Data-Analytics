import matplotlib.pyplot as plt
import numpy as np

# Σημεία δεδομένων
data = {
    "Point A": (30, 9),
    "Point B": (29, 3),
    "Point C": (41, 7),
}

# Δημιουργήστε διάγραμμα διασποράς
plt.figure(figsize=(12, 6))
for point, (x, y) in data.items():
    plt.scatter(x, y, label=point)
    plt.annotate(
        point, (x, y), textcoords="offset points", xytext=(0, 5), ha="center"
    )

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot with Annotations")
plt.legend()
plt.show()