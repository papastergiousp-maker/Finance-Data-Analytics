import plotly.graph_objects as go

# Data: Λίστα λεξικών που περιέχουν δεδομένα τοποθεσίας
location_data = [
    {"name": "London", "lat": 51.50, "lon": -0.12},
    {"name": "Paris", "lat": 48.85, "lon": 2.35},
    {"name": "Sydney", "lat": -33.87, "lon": 151.21},
]

# Δημιουργήστε ένα διάγραμμα Scattergeo
fig = go.Figure(
    go.Scattergeo(
        lat=[location["lat"] for location in location_data],
        lon=[location["lon"] for location in location_data],
        text=[location["name"] for location in location_data],
        mode="markers",
        marker=dict(
            size=15,
            color="rgba(0, 0, 255, 0.8)",
            line=dict(width=2, color="rgba(255, 255, 255, 0.8)"),
        ),
    )
)

# Προσαρμόστε την εμφάνιση του χάρτη
fig.update_geos(
    projection_type="natural earth",
    showcountries=True,
    countrycolor="rgb(204, 204, 204)",
    showcoastlines=True,
    coastlinecolor="rgb(204, 204, 204)",
    showland=True,
    landcolor="rgb(243, 243, 243)",
    showocean=True,
    oceancolor="rgb(217, 217, 217)",
)

# Ορίστε τη διάταξη του διαγράμματος
fig.update_layout(
    title="Geographic Locations",
    font=dict(family="Arial, sans-serif", size=12, color="rgb(37, 37, 37)"),
    hovermode="closest",
)

fig.show()