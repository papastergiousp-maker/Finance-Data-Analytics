import matplotlib.pyplot as plt

# Δεδομένα
organizations = ["Organization A", "Organization B", "Organization C"]
performance_metrics = [85, 102, 73]
colors = ['#2E8B57', '#4169E1', '#DC143C']  # Προσαρμοσμένα χρώματα
# Ραβδόγραμμα
plt.figure(figsize=(10, 6))
bars = plt.bar(organizations, performance_metrics, color=colors, edgecolor='black', linewidth=1)
# Προσθήκη τιμών πάνω από τις ράβδους
for i, (bar, value) in enumerate(zip(bars, performance_metrics)):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(value), 
             ha='center', va='bottom', fontsize=11, fontweight='bold')
# Τίτλοι και Ετικέτες
plt.title("Performance Metrics byOrganizations", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Organizations", fontsize=12, fontweight='bold')
plt.ylabel("Performance Metric", fontsize=12, fontweight='bold')
# Προσθήκη grid
plt.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
