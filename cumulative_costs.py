import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Initialize services and costs
services = ['Firestore', 'Pub/Sub', 'Big Query', 'Compute Engine Instance', 'Dataflow Workers']
costs = [574.17, 24.06, 98.15, 208.05, 90.05]

# Initialize month-year starting from July 2024
dates = pd.date_range(start='2024-07-01', periods=18, freq='ME')

df = pd.DataFrame()
df['MonthYear'] = np.repeat(dates, len(services))
df['Service'] = services*len(dates) 
df['Cost'] = np.tile(costs, len(dates))


df['CumulativeCost'] = df.groupby('Service')['Cost'].cumsum()

# Create a stacked bar chart
fig = px.bar(df, 
             x='MonthYear', 
             y='CumulativeCost', 
             color='Service',
             labels={'CumulativeCost': 'Cost (USD)', 'MonthYear': 'Month'},
             title='Cumulative Costs Per Month',
             color_discrete_sequence=['#FA9A26', '#FF736C', '#76CCBE', '#0A213D', '#1998DD', '#FB5350'])

# Calculate total costs for each month
total_monthly_costs = df.groupby('MonthYear')['Cost'].sum().reset_index()

# Add total cost scatter plot for annotations
fig.add_trace(go.Scatter(x=total_monthly_costs['MonthYear'],
                         y=total_monthly_costs['Cost'].cumsum(),
                         mode='text',
                         text=total_monthly_costs['Cost'].cumsum(),
                         textposition="top center",
                         texttemplate = "$%{text:,.2f}",
                         showlegend=False))

fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

# Add title
fig.update_layout(
    title={
        'text': "Monthly Costs per GCP Service for Booking Management System",
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_color="black",
    title_font_size=30)

fig.show()