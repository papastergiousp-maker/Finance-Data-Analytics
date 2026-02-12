# Εισάγετε τις απαραίτητες βιβλιοθήκες
import plotly.graph_objects as go
import numpy as np

# Προσομοιώστε τα δεδομένα
np.random.seed(42) # για αναπαραγωγιμότητα
n_stars = 500
x = np.random.normal(size=n_stars) # προσομοιώστε τις συντεταγμένες x των αστέρων
y = np.random.normal(size=n_stars) # προσομοιώστε τις συντεταγμένες y του αστέρα
z = np.random.normal(size=n_stars) # προσομοιώστε τις z-συντεταγμένες του αστέρα

# Προσομοιώστε τη θερμοκρασία του άστρου ως χρώμα
temp = np.random.randint(low=3000, high=6000, size=n_stars)
color = ['rgb({}, {}, 255)'.format(int(t/6000*255), int(t/6000*255)) for t in temp]

# Δημιουργήστε το σχήμα
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers',
                                   marker=dict(size=6, color=color, opacity=0.8))])

# Ενημερώστε τη διάταξη του σχήματος
fig.update_layout(title='Simulated Galaxy',
                  scene=dict(xaxis=dict(title='X'),
                             yaxis=dict(title='Y'),
                             zaxis=dict(title='Z')),
                  width=800,
                  height=800,
                  margin=dict(l=0, r=0, b=0, t=0))

fig.show()