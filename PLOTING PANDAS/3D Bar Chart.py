# Εισάγετε τις βιβλιοθήκες
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ορίστε τα δεδομένα
data = {
    "Goals": [22, 18, 12, 6, 4, 2],
    "Player": ["Lionel Messi", "Cristiano Ronaldo", "Luka Modric", 
               "N'Golo Kante", "Sergio Ramos", "Virgil van Dijk"],
    "Position": ["Forward", "Forward", "Midfielder", 
                 "Midfielder", "Defender", "Defender"]
}

# Δημιουργήστε DataFrame
df = pd.DataFrame(data)

# Δημιουργήστε το 3D διάγραμμα
fig = plt.figure(figsize=(24, 12))
ax = fig.add_subplot(111, projection="3d")

# Πάρτε τις μοναδικές θέσεις
positions = df["Position"].unique()
colors = ["darkorange", "lightgreen", "cyan"]

# Δημιουργήστε το 3D bar chart
for i, position in enumerate(positions):
    position_data = df[df["Position"] == position]
    x = np.arange(len(position_data))
    y = position_data["Goals"]
    z = np.zeros(len(position_data))
    dx = np.ones(len(position_data))
    dy = np.ones(len(position_data))
    dz = position_data["Goals"]
    
    ax.bar3d(x, y, z, dx, dy, dz, color=colors[i], shade=True)

# Προσθέστε ετικέτες
ax.set_xlabel("Player Index")
ax.set_ylabel("Goals")
ax.set_zlabel("Position")

# Εμφανίστε το διάγραμμα
plt.show()