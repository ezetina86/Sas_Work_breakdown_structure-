import plotly.figure_factory as ff
import datetime

# Define the tasks for each environment
tasks = [{'Task': 'Environment: dev', 
          'Start': datetime.datetime(2024, 5, 1), 
          'Finish': datetime.datetime(2025, 11, 1),
          'Resource': 'dev'},
         
         {'Task': 'Environment: stg', 
          'Start': datetime.datetime(2025, 1, 1), 
          'Finish': datetime.datetime(2025, 11, 1),
          'Resource': 'stg'},
         
         {'Task': 'Environment: prod', 
          'Start': datetime.datetime(2025, 4, 1), 
          'Finish': datetime.datetime(2025, 11, 1),
          'Resource': 'prod'}
         ]

# Assign a color to each environment in the dictionary
colors_dict = {'dev': '#FA9A26', 'stg': '#FF736C', 'prod': '#76CCBE'}

# Create a Gantt chart
fig = ff.create_gantt(tasks, 
                      index_col='Resource', 
                      colors=colors_dict, 
                      show_colorbar=True, 
                      group_tasks=True)

# Add title
fig.update_layout(
    title={
        'text': "Environments Usage Schedule",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_color="black",
    title_font_size=30)

# Show the Gantt chart with x-axis displaying time intervals per month.
fig.update_xaxes(
    tick0="2024-05-01",
    dtick="M1",  # represents one month
)

# Show the Gantt chart
fig.show()