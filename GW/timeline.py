import plotly.figure_factory as ff
import datetime

# Define project tasks
tasks = [
    dict(Task="Project Initiation and Planning", Start='2024-05-01', Finish='2024-05-14'),
    dict(Task="Requirements Gathering and Analysis", Start='2024-05-15', Finish='2024-06-05'),
    dict(Task="Solution Design", Start='2024-06-06', Finish='2024-07-31'),
    dict(Task="Solution Development", Start='2024-08-01', Finish='2024-11-27'),
    dict(Task="Integration & System Testing", Start='2024-11-28', Finish='2025-01-22'),
    dict(Task="User Acceptance Testing (UAT)", Start='2025-01-23', Finish='2025-02-05'),
    dict(Task="Deployment and Stabilization", Start='2025-02-06', Finish='2025-02-19'),
    dict(Task="Post-Production Support and Transition", Start='2025-02-20', Finish='2025-04-16')]

# Define task colors
colors = [
    "#00F6FF", "#00FFF0", "#B896FF", "#7BA8FF", "#060606", 
    "#0047FF", "#0078C2", "#8453D", "#4A71BD", "#FBFAFA"
]

# Create Gantt chart
fig = ff.create_gantt(tasks, colors=colors, title='Timeline for Product and Loncation management system', showgrid_x=True, showgrid_y=True)
fig.show()