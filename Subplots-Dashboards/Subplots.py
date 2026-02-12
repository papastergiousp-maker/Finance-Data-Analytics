import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Δημιουργία δεδομένων
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x/2)

# Δημιουργία subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Sin(x)', 'Cos(x)', 'Tan(x)', 'Exp(-x/2)'),
    specs=[[{"secondary_y": False}, {"secondary_y": False}],
           [{"secondary_y": False}, {"secondary_y": False}]]
)

# Προσθήκη traces
fig.add_trace(go.Scatter(x=x, y=y1, name='sin(x)', line=dict(color='blue')), row=1, col=1)
fig.add_trace(go.Scatter(x=x, y=y2, name='cos(x)', line=dict(color='red')), row=1, col=2)
fig.add_trace(go.Scatter(x=x, y=y3, name='tan(x)', line=dict(color='green')), row=2, col=1)
fig.add_trace(go.Scatter(x=x, y=y4, name='exp(-x/2)', line=dict(color='orange')), row=2, col=2)

# Ενημέρωση layout
fig.update_layout(
    title_text="Μαθηματικές Συναρτήσεις - Subplots",
    showlegend=False,
    height=600
)

fig.show()