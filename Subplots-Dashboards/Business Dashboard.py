import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Δημιουργία business data
months = ['Ιαν', 'Φεβ', 'Μαρ', 'Απρ', 'Μαι', 'Ιουν']
sales = [120, 135, 148, 162, 178, 195]
customers = [450, 520, 580, 640, 720, 800]
revenue = [15000, 18000, 22000, 25000, 28000, 32000]

# Δημιουργία dashboard με 4 subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Πωλήσεις', 'Πελάτες', 'Έσοδα', 'Τάσεις'),
    specs=[[{"type": "bar"}, {"type": "scatter"}],
           [{"type": "scatter"}, {"type": "scatter"}]]
)

# Bar chart για πωλήσεις
fig.add_trace(
    go.Bar(x=months, y=sales, name='Πωλήσεις', marker_color='lightblue'),
    row=1, col=1
)

# Line chart για πελάτες
fig.add_trace(
    go.Scatter(x=months, y=customers, mode='lines+markers', 
               name='Πελάτες', line=dict(color='green')),
    row=1, col=2
)

# Area chart για έσοδα
fig.add_trace(
    go.Scatter(x=months, y=revenue, fill='tonexty', 
               name='Έσοδα', line=dict(color='orange')),
    row=2, col=1
)

# Combined chart
fig.add_trace(
    go.Scatter(x=months, y=[s/10 for s in sales], 
               name='Πωλήσεις/10', line=dict(color='red')),
    row=2, col=2
)
fig.add_trace(
    go.Scatter(x=months, y=[c/100 for c in customers], 
               name='Πελάτες/100', line=dict(color='blue')),
    row=2, col=2
)

fig.update_layout(
    title_text="Business Analytics Dashboard",
    showlegend=False,
    height=700
)

fig.show()