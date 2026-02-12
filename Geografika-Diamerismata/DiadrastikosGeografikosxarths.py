import plotly.graph_objects as go

# Δεδομένα τοποθεσιών
locations = [
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
    {"name": "Sydney", "lat": -33.8688, "lon": 151.2093},
]
# Δημιουργία του διαδραστικού γεωγραφικού χάρτη
fig = go.Figure(go.Scattergeo(
    lat=[loc["lat"] for loc in locations],
    lon=[loc["lon"] for loc in locations],
    text=[loc["name"] for loc in locations],
    mode="markers",
    marker=dict(
        size=10,
        color="blue",
    ))
)
fig.update_geos(projection_type="equirectangular")
fig.show()