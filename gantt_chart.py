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

# Define the tasks 
tasks = [{'Task': 'Team Setup and Initial Scope', 
          'Start': datetime.datetime(2024, 5, 1), 
          'Finish': datetime.datetime(2024, 5, 30),
          'Resource': 'Project Manager, Business Analyst'},
         
         {'Task': 'Technical Pre-requisites and Non-functional Requirements', 
          'Start': datetime.datetime(2024, 5, 15),  # Start while setting up the team and initial scope
          'Finish': datetime.datetime(2024, 6, 15),
          'Resource': 'Solution Architect'},
         
         {'Task': 'Detailed Functional Requirements and Initial Estimation', 
          'Start': datetime.datetime(2024, 6, 1),  # Start before the previous task finishes
          'Finish': datetime.datetime(2024, 7, 1),
          'Resource': 'Functional Analyst, Solution Architect'},
         
         {'Task': 'Discovery Report Presentation and Project Kick-Off Meeting', 
          'Start': datetime.datetime(2024, 7, 1),  # Kick-off as soon as the initial estimation is done
          'Finish': datetime.datetime(2024, 8, 1),
          'Resource': 'Project Coordinator, Delivery Manager'},
         
         {'Task': 'Design a System That Meets Project’s Requirements', 
          'Start': datetime.datetime(2024, 7, 15),  # Start designing system in parallel with the kick-off meeting
          'Finish': datetime.datetime(2024, 11, 15),
          'Resource': 'Solution Architect'},
         
         {'Task': 'Coding and System Development', 
          'Start': datetime.datetime(2024, 11, 1),  # Start coding when system design is nearing completion
          'Finish': datetime.datetime(2025, 4, 1),
          'Resource': 'Developers'},
         
         {'Task': 'Conduct System Testing', 
          'Start': datetime.datetime(2025, 3, 15),  # Start testing before development is completely done
          'Finish': datetime.datetime(2025, 6, 15),
          'Resource': 'Quality Assurance team'},
         
         {'Task': 'Guided System Deployment', 
          'Start': datetime.datetime(2025, 6, 1),  # Start deployment when testing is still going on
          'Finish': datetime.datetime(2025, 7, 1),
          'Resource': 'Technical Support team'}]

# Reverse the tasks list
tasks = tasks[::-1]

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

# Show the Gantt chart with x-axis displaying time intervals per month.
fig.update_xaxes(
                tick0="2024-05-01",
                dtick="M1",  # represents one month
                )

# Show the Gantt chart
fig.show()