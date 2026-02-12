import plotly.graph_objects as go
# Ορίστε τα δεδομένα για το διάγραμμα
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 1, 5, 4]
z_values = [1, 3, 2, 4, 1] # Πρόσθετη διάσταση για το μέγεθος της φυσαλίδας
# Δημιουργήστε ένα διάγραμμα φυσαλίδων χρησιμοποιώντας τα δεδομένα
fig = go.Figure(
    go.Scatter(
        x=x_values,
        y=y_values,
        mode="markers",
        marker=dict(
            size=[a * 10 for a in z_values], # Ορίστε το μέγεθος των φυσαλίδων
            color=[0, 1, 2, 3, 4], # Ορίστε τα χρώματα των φυσαλίδων
            colorscale="Viridis",
            showscale=True # Εμφανίστε μια χρωματική κλίμακα
        )
    )
)
# Ενημερώστε τη διάταξη του διαγράμματος φυσαλίδων
fig.update_layout(
    title="A Simple Bubble Chart",
    xaxis_title="X Values",
    yaxis_title="Y Values",
)
# Εμφανίστε το διάγραμμα φυσαλίδων
fig.show()