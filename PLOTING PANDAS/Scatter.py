import pandas as pd
import matplotlib.pyplot as plt
# Δημιουργήστε τα δεδομένα
data = {'Age': [22, 24, 26, 28, 30, 32, 34],
        'Goals': [15, 20, 25, 30, 28, 22, 18]}
# Μετατρέψτε τα δεδομένα σε ένα pandas DataFrame
df = pd.DataFrame(data)
# Ορίστε το μέγεθος της φιγούρας
plt.figure(figsize=(12,6))
# Δημιουργήστε το scatter plot
plt.scatter(df['Age'], df['Goals'])
# Προσθέστε τίτλο και ετικέτες αξόνων
plt.title('Relationship Between Age and Goals Scored in a Season')
plt.xlabel('Age')
plt.ylabel('Goals Scored')
# Εμφανίστε το γράφημα
plt.show()