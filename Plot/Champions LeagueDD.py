import matplotlib.pyplot as plt

players = ['Lionel Messi', 'Cristiano Ronaldo', 'Robert Lewandowski', 'Kylian Mbappe', 'Erling Haaland']
goals = [12, 15, 16, 13, 14]
games = [10, 10, 10, 10, 10]
colors = ['darkblue', 'darkgreen', 'darkred', 'purple', 'darkorange']
markers = ['o', 'v', '^', '<', '>']

plt.figure(figsize=(10, 6))
for i in range(len(players)):
    plt.scatter(games[i], goals[i], color=colors[i], marker=markers[i], s=100, label=players[i])

plt.title('Goals Scored vs Games Played')
plt.xlabel('Games Played')
plt.ylabel('Goals Scored')
plt.legend()
plt.show()