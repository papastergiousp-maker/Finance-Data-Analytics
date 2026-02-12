import pandas as pd
import matplotlib.pyplot as plt
# Δημιουργήστε τα δεδομένα
data = {'Age': [22, 24, 26, 28, 30, 32, 34],
        'Goals': [15, 20, 25, 30, 28, 22, 18],
        'Assists': [5, 8, 10, 12, 11, 9, 7]}
# Μετατρέψτε τα δεδομένα σε ένα pandas DataFrame
df = pd.DataFrame(data)
# Ορίστε το μέγεθος της φιγούρας
fig = plt.figure(figsize=(24, 12))
ax = fig.add_subplot(111, projection='3d')
# Δημιουργήστε το 3D scatter plot
ax.scatter(df['Age'], df['Goals'], df['Assists'], c=df['Age'], cmap='viridis', s=100, edgecolor='k', alpha=0.75, linewidth=1)
# Προσθέστε τίτλο και ετικέτες αξόνων
ax.set_title('3D Scatter Plot of Age, Goals, and Assists in a Season', fontsize=20, pad=20)
ax.set_xlabel('Age', fontsize=14, labelpad=10)
ax.set_ylabel('Goals', fontsize=14, labelpad=10)
ax.set_zlabel('Assists', fontsize=14, labelpad=10)
plt.show()
