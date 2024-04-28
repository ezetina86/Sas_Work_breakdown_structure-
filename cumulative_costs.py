import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import timedelta

# Create a DataFrame with Monthly Costs per Environment
monthly_cost = pd.DataFrame({
    'Month': pd.date_range(start='05-2024', periods=18, freq='M'),
    'Environment': ['dev'] * 8 + ['dev, stg'] * 4 + ['dev, stg, prod'] * 6,
    'Cost': [497] * 8 + [1243] * 4 + [2238] * 6,
    'CumulativeCost': [497*i for i in range(1, 9)] + [3981+1243*i for i in range(1, 5)] + [9464+2238*i for i in range(1, 7)]
})

# Create a bar char
fig = go.Figure([go.Bar(
    x=monthly_cost['Month'], 
    y=monthly_cost['CumulativeCost'], 
    text=['$'+str(round(i/1000, 1))+'k' for i in monthly_cost['CumulativeCost']], 
    textposition='auto', 
    marker_color='#1998DD')])

# Center and bold the title
fig.update_layout(
    title={
        'text': 'Cumulative Monthly Costs per Environment',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        title_font_size=20
)

fig.show()