import plotly.figure_factory as ff
import datetime

# Update your color dictionary to have a color for each distinct 'Resource' used
colors_dict = {'Project Manager, Business Analyst': '#FA9A26',
               'Solution Architect': '#FF736C',
               'Functional Analyst, Solution Architect': '#FB5350',
               'Project Coordinator, Delivery Manager': '#0A213D',
               'Developers': '#1998DD',
               'Quality Assurance team': '#76CCBE',
               'Technical Support team': '#76CCBE',
               'Project Manager': '#FA9A26'} 

# Define tasks
tasks = [{'Task': 'Team Setup and Initial Scope', 
          'Start': datetime.datetime(2024, 5, 1), 
          'Finish': datetime.datetime(2024, 5, 30),
          'Resource': 'Project Manager, Business Analyst'},
         {'Task': 'Technical Pre-requisites and Non-functional Requirements', 
          'Start': datetime.datetime(2024, 5, 30), 
          'Finish': datetime.datetime(2024, 6, 30),
          'Resource': 'Solution Architect'},
         {'Task': 'Detailed Functional Requirements and Initial Estimation', 
          'Start': datetime.datetime(2024, 6, 30), 
          'Finish': datetime.datetime(2024, 7, 30),
          'Resource': 'Functional Analyst, Solution Architect'},
         {'Task': 'Discovery Report Presentation and Project Kick-Off Meeting', 
          'Start': datetime.datetime(2024, 7, 30), 
          'Finish': datetime.datetime(2024, 8, 30),
          'Resource': 'Project Coordinator, Delivery Manager'},
         {'Task': 'Design a System That Meets Project’s Requirements', 
          'Start': datetime.datetime(2024, 8, 30), 
          'Finish': datetime.datetime(2024, 12, 30),
          'Resource': 'Solution Architect'},
         {'Task': 'Coding and System Development', 
          'Start': datetime.datetime(2024, 12, 30), 
          'Finish': datetime.datetime(2025, 5, 30),
          'Resource': 'Developers'},
         {'Task': 'Conduct System Testing', 
          'Start': datetime.datetime(2025, 5, 30), 
          'Finish': datetime.datetime(2025, 8, 30),
          'Resource': 'Quality Assurance team'},
         {'Task': 'Guided System Deployment', 
          'Start': datetime.datetime(2025, 8, 30), 
          'Finish': datetime.datetime(2025, 9, 30),
          'Resource': 'Technical Support team'}]

# Create a Gantt chart
fig = ff.create_gantt(tasks, 
                      index_col='Resource', 
                      colors=colors_dict, 
                      show_colorbar=True, 
                      group_tasks=False, 
                      showgrid_x=True)

# Add title
fig.update_layout(
    title={
        'text': "Booking Management System Schedule",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    title_font_family="Times New Roman",
    title_font_color="black",
    title_font_size=30)


# Show the Gantt chart
fig.show()