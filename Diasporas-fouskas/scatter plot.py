import plotly.graph_objects as go # Εισάγετε την ενότητα graph_objects από τη βιβλιοθήκη plotly

# Ορίστε τα δεδομένα για το διάγραμμα διασποράς
x_values = [1, 2, 3, 4, 5] # Λίστα τιμών x
y_values = [2, 3, 1, 5, 4] # Λίστα τιμών y

# Δημιουργήστε ένα διάγραμμα διασποράς χρησιμοποιώντας τα δεδομένα
fig = go.Figure(
    go.Scatter(
        x=x_values,
        y=y_values,
        mode="markers",
        marker=dict(
            size=15, 
            color= [0,1,2,3,4], # Ορίστε τα χρώματα των δεικτών
            colorscale="Viridis",
            showscale=True # Εμφανίστε μια χρωματική κλίμακα
        )
    )
)

# Ενημερώστε τη διάταξη του διαγράμματος διασποράς
fig.update_layout(
    title="A Simple Scatter Plot",
    xaxis_title="X Values",
    yaxis_title="Y Values",
)

# Εμφανίστε το διάγραμμα διασποράς
fig.show()