
# Εισάγετε τις βιβλιοθήκες
import plotly.graph_objects as go
import pandas as pd

# Δημιουργήστε ένα λεξικό με δεδομένα πωλήσεων και κερδών για τέσσερα προϊόντα
data = {
    "Product": ["Product A", "Product B", "Product C", "Product D"],
    "Sales": [2000, 2500, 1800, 2200],
    "Profit": [500, 700, 400, 600],
}

# Μετατρέψτε το λεξικό σε pandas DataFrame
df = pd.DataFrame(data)

# Δημιουργήστε ένα αντικείμενο plotly Figure
fig = go.Figure()

# Προσθέστε ένα ίχνος ράβδων για τις πωλήσεις
fig.add_trace(
    go.Bar(
        x=df["Product"],
        y=df["Sales"],
        name="Sales",
        marker=dict(color="blue", line=dict(color="#000000", width=1)),
    )
)

# Προσθέστε ένα ίχνος μπάρας για το κέρδος
fig.add_trace(
    go.Bar(
        x=df["Product"],
        y=df["Profit"],
        name="Profit",
        marker=dict(color="red", line=dict(color="#000000", width=1)),
    )
)

# Ενημερώστε τη διάταξη του σχήματος
fig.update_layout(
    title="Sales and Profit in 2020",
    xaxis_title="Product",
    yaxis_title="Values",
    plot_bgcolor="rgba(0, 0, 0, 0)",
    hovermode="x unified",
    barmode="group",
)

# Εμφανίστε το σχήμα
fig.show()