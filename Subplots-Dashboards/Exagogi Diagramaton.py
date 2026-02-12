import plotly.graph_objects as go
import plotly.io as pio

# Δημιουργία διαγράμματος
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[2, 4, 3, 5, 6],
    mode='lines+markers',
    name='Δεδομένα'
))

fig.update_layout(
    title="Διάγραμμα για Εξαγωγή",
    xaxis_title="X Άξονας",
    yaxis_title="Y Άξονας"
)

# Εξαγωγή σε HTML
fig.write_html("my_plot.html")

# Εξαγωγή σε PNG (χρειάζεται kaleido)
# fig.write_image("my_plot.png", width=800, height=600)

# Εξαγωγή σε PDF
# fig.write_image("my_plot.pdf")

# Εξαγωγή σε SVG
# fig.write_image("my_plot.svg")

# Εξαγωγή σε JSON
fig.write_json("my_plot.json")

print("Διάγραμμα εξήχθη επιτυχώς!")