# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ### Kickstarter Success
            Kickstarter Success is an application that leverages machine learning to help predict if a kickstarter 
            campaign is likely to be successful based on monetary goal, campaign length, and other features.


             


            Check it out!

            """
        ),

        dcc.Link(dbc.Button('Kickstarter Success Predictor', color='primary'), href='/Predictions')
    ],
    md=5,
)



column2 = dbc.Col(
    [

    ],
    md=1,
)

column3 = dbc.Col(
    [
        html.Img(src='assets/kickstarter.png', className='img-fluid'),

    ],
    md=6,
)

layout = dbc.Row([column1, column2, column3])