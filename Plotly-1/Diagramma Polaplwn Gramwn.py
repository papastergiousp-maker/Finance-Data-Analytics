# Εισάγετε τις βιβλιοθήκες
import plotly.graph_objects as go
import pandas as pd

# Δημιουργήστε ένα λεξικό με δεδομένα πωλήσεων για τρία προϊόντα για τέσσερα χρόνια
data = {
    'Year': [2017, 2018, 2019, 2020],
    'Product A': [2000, 2500, 2700, 3000],
    'Product B': [1500, 1800, 2100, 2400],
    'Product C': [1800, 2100, 2300, 2500]
}

# Μετατρέψτε το λεξικό σε pandas DataFrame
df = pd.DataFrame(data)

# Δημιουργήστε ένα νέο αντικείμενο plotly Figure
fig = go.Figure()

# Προσθέστε ένα ίχνος για τις πωλήσεις κάθε προϊόντος
for product in ['Product A', 'Product B', 'Product C']:
    fig.add_trace(go.Scatter(x=df['Year'], y=df[product], mode='lines+markers', name=product))

# Ενημερώστε τη διάταξη του σχήματος
fig.update_layout(title='Sales per Year',
                  xaxis_title='Year',
                  yaxis_title='Sales',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  hovermode='x unified')

# Εμφανίστε το σχήμα
fig.show()