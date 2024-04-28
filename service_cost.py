import pandas as pd
import numpy as np
import plotly.express as px

# Monthly costs for each service in prod
prod_costs = {
    'Firestore (Storage/Read/Write/Delete)': 574.17,
    'Pub/Sub': 24.06,
    'Big Query (Analysis+Storage)': 98.15,
    'Compute Engine Instance (Core+Ram)': 208.05,
    'Dataflow Workers': 90.05
}

# Calculate costs for dev and stg environments (development is 50% of prod, staging is 75% of prod)
dev_costs = {service: 0.5 * cost for service, cost in prod_costs.items()}
stg_costs = {service: 0.75 * cost for service, cost in prod_costs.items()}

# Add to the dataframe
df_prod = pd.DataFrame(list(prod_costs.items()), columns=['Service', 'Cost'])
df_prod['Environment'] = 'prod'
df_dev = pd.DataFrame(list(dev_costs.items()), columns=['Service', 'Cost'])
df_dev['Environment'] = 'dev'
df_stg = pd.DataFrame(list(stg_costs.items()), columns=['Service', 'Cost'])
df_stg['Environment'] = 'stg'

df = pd.concat([df_prod, df_dev, df_stg])

# Create a pie chart
fig = px.pie(df, values='Cost', names='Service', 
             title='Monthly Costs per Service for Booking Management System', 
             color_discrete_sequence=['#FA9A26', '#FF736C', '#76CCBE', '#0A213D', '#1998DD', '#FB5350'])

# Update the labels to include only the amount and percentage (not the service name)
fig.update_traces(textinfo='value+percent', hoverinfo='label+value+percent',
                  texttemplate="$%{value:,.2f}")


# Add title
fig.update_layout(
    title={
        'text': "Monthly Costs per Service for Booking Management System",
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_color="black",
    title_font_size=30)

fig.show()