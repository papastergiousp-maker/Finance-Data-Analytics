import plotly.graph_objects as go
import pandas as pd
# Προσομοίωση dataset
data = {
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "lat": [40.7128, 34.0522, 41.8781, 29.7604, 33.4484],
    "lon": [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740],
    "temperature": [25, 30, 28, 33, 38]
}
df = pd.DataFrame(data)
fig = go.Figure(go.Scattergeo(
    lon = df['lon'],
    lat = df['lat'],
    text = df['city'],
    mode = 'markers',
    marker = dict(
        size = df['temperature'],
        color = df['temperature'],
        colorscale = 'Viridis',
        showscale = True,
        colorbar_title = "Temperature (°C)"
    )
))
fig.update_layout(
    title_text = 'Real-time Weather Data visualization',
    geo_scope='usa',
)
fig.show()
