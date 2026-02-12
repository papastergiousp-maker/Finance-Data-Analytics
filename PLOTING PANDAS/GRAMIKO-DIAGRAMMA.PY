# Εισάγετε τις απαιτούμενες βιβλιοθήκες
import pandas as pd
import matplotlib.pyplot as plt

# Δημιουργήστε ένα λεξικό που περιέχει τα δεδομένα
data = {'Year': [2016, 2017, 2018, 2019, 2020],
        'Goals': [25, 30, 28, 35, 32]}
# Μετατρέψτε το λεξικό σε ένα pandas DataFrame
df = pd.DataFrame(data)
# Ορίστε το μέγεθος της φιγούρας
plt.figure(figsize=(12, 6))
# Δημιουργήστε το γράφημα γραμμής
plt.plot(df['Year'], df['Goals'])
# Προσθέστε τίτλο και ετικέτες αξόνων
plt.xlabel('Year')
plt.ylabel('Goals')
plt.title('Goals Scored by a Soccer Player Over Years')
# Εμφανίστε το γράφημα
plt.show()