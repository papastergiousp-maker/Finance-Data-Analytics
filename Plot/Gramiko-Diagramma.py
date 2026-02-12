import matplotlib.pyplot as plt

# Δεδομένα
years = [2018, 2019, 2020, 2021, 2022]
person_A_performance = [37, 34, 36, 25, 30]
person_B_performance = [25, 26, 21, 31, 29]

# Γραμμικό Διάγραμμα
plt.figure(figsize=(12, 6))
plt.plot(years, person_A_performance, marker='o', label='Person A', linewidth=2)
plt.plot(years, person_B_performance, marker='s', label='Person B', linewidth=2)

# Τίτλοι, Ετικέτες και Υπόμνημα
plt.title("Performance Metrics of Person A and Person B (2018-2022)", 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12, fontweight='bold')
plt.ylabel("Performance Metric", fontsize=12, fontweight='bold')
plt.legend(loc='upper right', fontsize=11, frameon=True)

# Προσθήκη grid για καλύτερη αναγνωσιμότητα
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()