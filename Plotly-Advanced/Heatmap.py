import plotly.graph_objects as go
import plotly.express as px
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

fig = go.Figure(data=go.Heatmap(
    z=data, 
    colorscale='Viridis', 
    hoverongaps=False
))

fig.show()