import pandas as pd
import matplotlib.pyplot as plt
data = {'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar', 'Kylian Mbappe'],
        'Goals': [36, 31, 23, 33]}
df = pd.DataFrame(data)
plt.figure(figsize=(12,6))
plt.bar(df['Player'], df['Goals'])
plt.title('Goals Scored by Top Soccer Players in a Season')
plt.xlabel('Player')
plt.ylabel('Goals')
plt.show()
