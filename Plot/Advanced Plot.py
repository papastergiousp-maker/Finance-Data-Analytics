import matplotlib.pyplot as plt
import numpy as np

# Δεδομένα
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_2022 = [120, 135, 148, 162, 158, 175]
sales_2023 = [110, 142, 155, 168, 172, 185]

# Δημιουργία γραφήματος
plt.figure(figsize=(12, 7))
plt.plot(months, sales_2022, marker='o', linewidth=3, markersize=8, 
         label='Sales 2022', color='#1f77b4')
plt.plot(months, sales_2023, marker='s', linewidth=3, markersize=8, 
         label='Sales 2023', color='#ff7f0e')

# Προχωρημένη προσαρμογή τίτλου
plt.title("Monthly Sales Comparison: 2022 vs 2023", 
          fontsize=18, fontweight='bold', pad=25, 
          color='darkblue', family='serif')

# Προχωρημένη προσαρμογή ετικετών
plt.xlabel("Month", fontsize=14, fontweight='bold', 
           color='darkgreen', labelpad=10)
plt.ylabel("Sales (in thousands)", fontsize=14, fontweight='bold', 
           color='darkgreen', labelpad=10)

# Προχωρημένη προσαρμογή υπομνήματος
plt.legend(loc='lower right', fontsize=12, frameon=True, 
           fancybox=True, shadow=True, framealpha=0.9,
           facecolor='lightgray', edgecolor='black')

# Προσθήκη grid και άλλων στοιχείων
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Προσαρμογή περιθωρίων
plt.tight_layout()

plt.show()