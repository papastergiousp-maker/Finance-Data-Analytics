import matplotlib.pyplot as plt

players = ['Lionel Messi', 'Cristiano Ronaldo', 'Robert Lewandowski', 'Kylian Mbappe', 'Erling Haaland']
goals = [12, 15, 16, 13, 14]

plt.figure(figsize=(10, 6))
plt.plot(players, goals, marker='o', label='Goals')
plt.title('Goals Scored by Players in the Champions League')
plt.xlabel('Players')
plt.ylabel('Goals Scored')
plt.legend()
plt.show()