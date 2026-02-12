# Εισάγετε τις βιβλιοθήκες
import plotly.graph_objects as go
import pandas as pd

# Δημιουργήστε ένα λεξικό με τα μερίδια αγοράς για τέσσερα προϊόντα
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Market Share': [30, 20, 25, 25]
}

# Μετατρέψτε το λεξικό σε ένα πλαίσιο δεδομένων pandas DataFrame
df = pd.DataFrame(data)

# Δημιουργήστε ένα αντικείμενο Plotly Figure
fig = go.Figure()

# Προσθέστε ένα ίχνος Πίτας (Donut) στο σχήμα
fig.add_trace(go.Pie(
    labels=df['Product'],
    values=df['Market Share'],
    hole=0.3, # Αυτό δημιουργεί το σχήμα "donut"
    textinfo='label+percent',
    marker=dict(colors=['blue', 'red', 'green', 'purple'])
))

# Ενημερώστε τη διάταξη του σχήματος
fig.update_layout(
    title='Market Share of Products',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    hovermode='x unified'
)
# Εμφανίστε το σχήμα
fig.show()