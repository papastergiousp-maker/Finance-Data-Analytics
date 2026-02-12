import plotly.graph_objects as go
fig = go.Figure(go.Scatter3d(
    x=[1, 2, 3, 4, 5],
    y=[10, 11, 12, 13, 14],
    z=[5, 6, 7, 8, 9],
    mode='markers',
    marker=dict(
        size=5,
        color=[100, 200, 300, 400, 500],
        colorscale='Viridis',
        showscale=True
    )
))

fig.show()