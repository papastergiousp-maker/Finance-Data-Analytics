import matplotlib.pyplot as plt
import numpy as np

# Σημεία δεδομένων
years = np.arange(2010, 2021)
values = [53, 73, 60, 41, 58, 41, 37, 45, 51, 31, 30]

plt.figure(figsize=(12, 6))
plt.plot(years, values, marker='o', label='Values')

# Προσθέστε βέλος
plt.arrow(2014, 58, 0, -17, length_includes_head=True, head_width=0.5, head_length=2, color='red')

plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Line Plot with Arrow')
plt.legend()
plt.show()