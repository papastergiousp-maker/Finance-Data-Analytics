import pandas as pd
import plotly.graph_objects as go

data = {
    "Sales": [1200, 1500, 900, 1800, 1600],
}
df = pd.DataFrame(data)

trace = go.Histogram(
    x=df["Sales"],
    nbinsx=5,
    name="Product Sales",
    marker=dict(color="#ff7f0e"),
)
layout = go.Layout(title="Product Sales Distribution")
fig = go.Figure(data=[trace], layout=layout)
fig.show()