import pandas as pd
import plotly.graph_objects as go

data = {
    "Salary": [34000, 36000, 29000, 22000, 28000, 30000, 40000, 35000, 37000, 32000],
}
df = pd.DataFrame(data)
trace = go.Box(
    y=df["Salary"],
    name="Employe Salary",
    marker=dict(color="#ff7f0e"),
)
layout = go.Layout(title="Employee Salary Distribution")
fig = go.Figure(data=[trace], layout=layout)
fig.show()