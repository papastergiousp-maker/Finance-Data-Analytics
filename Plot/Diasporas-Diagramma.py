import matplotlib.pyplot as plt
# Δεδομένα
individuals = ["Person A", "Person B", "Person C", "Person D"]
variable_1 = [30, 29, 13, 18]
variable_2 = [9, 2, 20, 12]
# Διάγραμμα Διασποράς
plt.figure(figsize=(10, 6))
plt.scatter(individuals, variable_1, color='red', s=100, label='Variable 1', alpha=0.7, edgecolors='b')
# Προσθήκη σχολιασμών
for i, individual in enumerate(individuals):
    plt.annotate(individual, (variable_1[i], variable_2[i]), textcoords="offset points", xytext=(5, 5), fontsize=10, fontweight='bold')
# Τίτλοι και Ετικέτες
plt.title("Variable 1 vs Variable 2 Comparison", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Variable 1", fontsize=12, fontweight='bold')
plt.ylabel("Variable 2", fontsize=12, fontweight='bold')
# Προσθήκη grid
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()