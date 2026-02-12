import pandas as pd
import plotly.express as px
# Προσομοίωση dataset
data = {
    "country": ["China", "India", "USA", "Indonesia", "Pakistan", 
                "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"],
    "population": [1393000000, 1366000000, 331000000, 273000000, 225000000, 
                   213000000, 211000000, 166000000, 146000000, 130000000]
}
df = pd.DataFrame(data)
fig = px.choropleth(df, locations="country",
                    locationmode='country names',
                    color="population",
                    title="World Population Visualization",
                    hover_name="country",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    projection="natural earth")
fig.show()