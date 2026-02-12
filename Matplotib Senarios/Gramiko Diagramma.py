import matplotlib.pyplot as plt
import numpy as np
players = ["Harry Kane", "Mo Salah", "Bruno Fernandes", "Jamie Vardy", "Son Heung-min"]
goals = [23, 25, 21, 22, 19]  # Γκολ (σεζόν)
plt.figure(figsize=(10, 6))
plt.plot(players, goals, marker='o', linestyle='-', color='b')
plt.title('Goals Scored by EPL Players in the Season')
plt.xlabel('Players')
plt.ylabel('Goals Scored')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()