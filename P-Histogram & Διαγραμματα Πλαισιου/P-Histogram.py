import pandas as pd
import plotly.graph_objects as go

data = {
    "Age": [22, 24, 35, 45, 67, 72, 51, 48, 56, 33],
}
df = pd.DataFrame(data)

trace = go.Histogram(
    x=df["Age"],
    nbinsx=5,
    name="Age Distribution",
    marker=dict(color="#1f77b4"),
)
layout = go.Layout(title="Population Age Distribution")
fig = go.Figure(data=[trace], layout=layout)
fig.show()