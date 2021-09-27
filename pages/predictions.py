import joblib
from joblib import load
import web_app
from web_app import assets
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from category_encoders import OrdinalEncoder
from xgboost import XGBClassifier
import shap

from app import app
from joblib import load

model = load('/Users/youssefalyakoob/Desktop/Kickstarter/web_app/xgb_model')
shap_model = load('/Users/youssefalyakoob/Desktop/Kickstarter/web_app/shap_model')
sub_category_list = [
    # 1 Art--Done
    [{'label': 'Ceramics', 'value': 17},
     {'label': 'Conceptual Art', 'value': 26},
     {'label': 'Digital Art', 'value': 31}, {'label': 'Illustration', 'value': 61},
     {'label': 'Mixed Media', 'value': 77}, {'label': 'Painting', 'value': 85},
     {'label': 'Performance Art', 'value': 87},
     {'label': 'Public Art', 'value': 102}, {'label': 'Sculpture', 'value': 115},
     {'label': 'Social Practice', 'value': 118},
     {'label': 'Textiles', 'value': 127}, {'label': 'Video Art', 'value': 134}],
    # 2 Comic
    [{'label': 'Anthologies', 'value': 6}, {'label': 'Comic books', 'value': 24},
     {'label': 'Events', 'value': 39}, {'label': 'Graphic Novels', 'value': 57},
     {'label': 'Webcomics', 'value': 139}],
    # 3 Crafts
    [{'label': 'Candles', 'value': 16}, {'label': 'Crochet', 'value': 30},
     {'label': 'DIY', 'value': 32}, {'label': 'Glass', 'value': 55},
     {'label': 'Knitting', 'value': 69}, {'label': 'Pottery', 'value': 98},
     {'label': 'Printing', 'value': 100},
     {'label': 'Stationery', 'value': 123}, {'label': 'Woodworking', 'value': 141}],
    # 4 Dance
    [{'label': 'Performances', 'value': 88},
     {'label': 'Residencies', 'value': 109}, {'label': 'Spaces', 'value': 122},
     {'label': 'Workshops', 'value': 142}],
    #  5 Design
    [{'label': 'Architecture', 'value': 9}, {'label': 'Design', 'value': 4},
     {'label': 'Graphic Design', 'value': 56}, {'label': 'Interactive Design', 'value': 65},
     {'label': 'Product Design', 'value': 101}, {'label': 'Typography', 'value': 131}],
    # 6 Fashion
    [{'label': 'Accessories', 'value': 2}, {'label': 'Apparel', 'value': 7},
     {'label': 'Childrenswear', 'value': 19},
     {'label': 'Couture', 'value': 29}, {'label': 'Footwear', 'value': 52},
     {'label': 'Jewelry', 'value': 67}, {'label': 'Ready-to-Wear', 'value': 108}],
    # 7 Films and Videos
    [{'label': 'Action', 'value': 3}, {'label': 'Animation', 'value': 5},
     {'label': 'Comedy', 'value': 23},
     {'label': 'Documentary', 'value': 34}, {'label': 'Drama', 'value': 35},
     {'label': 'Experimental', 'value': 40},
     {'label': 'Family', 'value': 43}, {'label': 'Fantasy', 'value': 44},
     {'label': 'Festivals', 'value': 47},
     {'label': 'Horror', 'value': 60},
     {'label': 'Movie Theaters', 'value': 79},
     {'label': 'Music Videos', 'value': 80}, {'label': 'Narrative Film', 'value': 82},
     {'label': 'Romance', 'value': 113},
     {'label': 'Science Fiction', 'value': 114}, {'label': 'Shorts', 'value': 116},
     {'label': 'Television', 'value': 126},
     {'label': 'Thrillers', 'value': 128}, {'label': 'Webseries', 'value': 140}],
    # 7 Food
    [{'label': 'Bacon', 'value': 12}, {'label': 'Community-Gardens', 'value': 25},
     {'label': 'Cookbooks', 'value': 27},
     {'label': 'Drinks', 'value': 36}, {'label': 'Events', 'value': 39},
     {'label': "Farmer's Markets", 'value': 45},
     {'label': 'Farms', 'value': 46},
     {'label': 'Food Trucks', 'value': 51},
     {'label': 'Restaurants', 'value': 110}, {'label': 'Small Batch', 'value': 117},
     {'label': 'Spaces', 'value': 122},
     {'label': 'Vegan', 'value': 132}],
    # 8 Games
    [{'label': 'Gaming Hardware', 'value': 54},
     {'label': 'Live Games', 'value': 74},
     {'label': 'Mobile Games', 'value': 78}, {'label': 'Playing Cards', 'value': 94},
     {'label': 'Puzzles', 'value': 104},
     {'label': 'Tabletop Games', 'value': 124}, {'label': 'Video Games', 'value': 135}],
    #  Journalism
    [{'label': 'Audio', 'value': 11},
     {'label': 'Photo', 'value': 91},
     {'label': 'Print', 'value': 99}, {'label': 'Video', 'value': 133},
     {'label': 'Web', 'value': 138}],
    #  Music
    [{'label': 'Blues', 'value': 13},
     {'label': 'Classical Music', 'value': 22},
     {'label': 'Country & Folk', 'value': 28},
     {'label': 'Electronic Music', 'value': 37},
     {'label': 'Faith', 'value': 42}, {'label': 'Hip-Hop', 'value': 59},
     {'label': 'Indie Rock', 'value': 63},
     {'label': 'Jazz', 'value': 66}, {'label': 'Kids', 'value': 68},
     {'label': 'Latin', 'value': 70},
     {'label': 'Metal', 'value': 76},
     {'label': 'Pop', 'value': 97},
     {'label': 'Punk', 'value': 103}, {'label': 'R&B', 'value': 106},
     {'label': 'Rock', 'value': 112},
     {'label': 'World Music', 'value': 143}],
    #  Photography
    [{'label': 'Animals', 'value': 4}, {'label': 'Fine Art', 'value': 49},
     {'label': 'Nature', 'value': 83},
     {'label': 'People', 'value': 86}, {'label': 'Photobooks', 'value': 92},
     {'label': 'Places', 'value': 93}],
    #  Publishing
    [{'label': 'Anthologies', 'value': 6},
     {'label': 'Art Books', 'value': 10},
     {'label': 'Calendars', 'value': 14}, {'label': "Children's Books", 'value': 18},
     {'label': 'Fiction', 'value': 48},
     {'label': 'Literary Journals', 'value': 72},
     {'label': 'Nonfiction', 'value': 84},
     {'label': 'Periodicals', 'value': 89},
     {'label': 'Poetry', 'value': 96},
     {'label': 'Radio & Podcasts', 'value': 107},
     {'label': 'Translations', 'value': 130}, {'label': 'Young Adult', 'value': 144},
     {'label': 'Zines', 'value': 145}],
    #  Technology
    [{'label': '3D Printing', 'value': 0}, {'label': 'Apps', 'value': 8},
     {'label': 'Camera Equipment', 'value': 15},
     {'label': 'DIY Electronics', 'value': 33}, {'label': 'Fabrication Tools', 'value': 41},
     {'label': 'Flight', 'value': 50},
     {'label': 'Gadgets', 'value': 53}, {'label': 'Hardware', 'value': 58},
     {'label': 'Makerspaces', 'value': 75},
     {'label': 'Robots', 'value': 111}, {'label': 'Software', 'value': 119},
     {'label': 'Sound', 'value': 120},
     {'label': 'Space Exploration', 'value': 121},
     {'label': 'Wearables', 'value': 136},
     {'label': 'Web', 'value': 138}],
    #  Theater
    [{'label': 'Comedy', 'value': 23}, {'label': 'Experimental', 'value': 40},
     {'label': 'Festivals', 'value': 47},
     {'label': 'Immersive', 'value': 62}, {'label': 'Musical', 'value': 81},
     {'label': 'Plays', 'value': 95},
     {'label': 'Spaces', 'value': 122}]]
column1 = dbc.Col(
    [
        dcc.Markdown('''###### Category'''),
        dcc.Dropdown(
            id='category-dropdown',
            options=[
                {'label': 'Art', 'value': 0},
                {'label': 'Comics', 'value': 1},
                {'label': 'Crafts', 'value': 2},
                {'label': 'Dance', 'value': 3},
                {'label': 'Design', 'value': 4},
                {'label': 'Fashion', 'value': 5},
                {'label': 'Films & Videos', 'value': 6},
                {'label': 'Food', 'value': 7},
                {'label': 'Games', 'value': 8},
                {'label': 'Journalism', 'value': 9},
                {'label': 'Music', 'value': 10},
                {'label': 'Photography', 'value': 11},
                {'label': 'Publishing', 'value': 12},
                {'label': 'Technology', 'value': 13},
                {'label': 'Theater', 'value': 14},
            ], value=0,
            className='mb-4'),
        dcc.Markdown('###### Sub-Category'),
        dcc.Dropdown(
            id='sub-category-dropdown',
            className='mb-5',
            value=0
        ),

        dcc.Markdown('''###### Funding Goal (USD)'''),
        dcc.Slider(
            id='goal-slider',
            min=0,
            max=100000,
            step=50,
            value=50,
        ),
        dcc.Markdown('', id='goal-slider-container'),

        dcc.Markdown('''###### Campaign Duration'''),
        dcc.Slider(
            id='campaign-duration-slider',
            min=2,
            max=100,
            step=1,
            value=2,
        ),
        dcc.Markdown('', id='campaign-duration-slider-container'),

    ],
)

column3 = dbc.Col(
    [

        # dcc.Markdown('',id='prediction-content', style={
        # 'textAlign':'center',
        # 'font-size':30}),

        html.H2('Campaign Success Likelihood', className='mb-5'),
        html.Div(id='prediction-content', className='lead')

    ],

)


# Creates options for sub category based on category list
@app.callback(
    Output('sub-category-dropdown', 'options'),
    [Input('category-dropdown', 'value')])
def set_cities_options(select_category):
    print(select_category)
    return sub_category_list[select_category]


# Takes inputs from user and returning to show their selection
@app.callback(
    dash.dependencies.Output('goal-slider-container', 'children'),
    [dash.dependencies.Input('goal-slider', 'value')])
def update_output(value):
    return 'Goal(USD) = "{}"'.format(value)


@app.callback(
    dash.dependencies.Output('campaign-duration-slider-container', 'children'),
    [dash.dependencies.Input('campaign-duration-slider', 'value')])
def update_output(value):
    return 'Campaign Duration = "{}"'.format(value)


@app.callback(
    Output('prediction-content', 'children'),
    [Input('category-dropdown', 'value'),
     Input('campaign-duration-slider', 'value'),
     Input('goal-slider', 'value'),
     Input('sub-category-dropdown', 'value'),

     ])
def predict(category, campaign_duration,
            goal_in_usd, sub_category):
    # backers_count, category, campaign_duration,
    # goal_in_usd, blurb_length, sub_category, usd_pledged,
    df = pd.DataFrame(columns=["category", "goal_in_usd",
                               "sub_category", "campaign_duration"],
                      data=[[category, goal_in_usd,
                             sub_category, campaign_duration]])

    y_pred = model.predict(df)[0]
    y_pred_prob = model.predict_proba(df)[0] * 100
    # explainer = shap.TreeExplainer(shap_model)
    # shap_values = explainer.shap_values(df)
    # shap.initjs()
    # return (shap.force_plot(base_value=explainer.expected_value,
    #             shap_values=shap_values,
    #             features = df.loc[0])

    if y_pred == 1:

        return f'you are {y_pred_prob[1]:.2f} % likely to succeed'




    else:
        return f'you are {y_pred_prob[0]:.2f} % likely to fail'


layout = dbc.Row([column1, column3])
