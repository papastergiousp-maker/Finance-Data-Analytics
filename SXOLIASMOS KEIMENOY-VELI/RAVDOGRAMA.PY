import matplotlib.pyplot as plt
import numpy as np

# Σημεία δεδομένων
data = {'A': 86, 'B': 74, 'C': 69}

# Δημιουργήστε ραβδόγραμμα
labels = list(data.keys())
values = list(data.values())
x = np.arange(len(labels))

plt.figure(figsize=(12, 6))
plt.bar(x, values)
plt.xticks(x, labels)

# Προσθέστε σχολιασμό κειμένου
for i, v in enumerate(values):
    plt.annotate(str(v), (i, v), textcoords="offset points", xytext=(0, 5), ha='center')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot with Annotations')
plt.show()