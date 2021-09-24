# Imports from 3rd party libraries

# from joblib import load
# pipeline = load('assets/pipeline_joblib')
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from templates import index, predictions

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='Using Machine Learning to Predict Kickstarter Success',
    brand_href='/',
    children=[
        dbc.NavItem(dcc.Link('Kickstarter Success Predictor', href='/Predictor', className='nav-link')),
        #dbc.NavItem(dcc.Link('Insights', href='/Insights', className='nav-link')),
        dbc.NavItem(dcc.Link('About', href='/About', className='nav-link')),
        # dbc.NavItem(dcc.Link('Result', href='/Result', className='nav-link'))
    ],
    sticky='top',
    color='light',
    light=True,
    dark=False
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Mark Porath', className='mr-2'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/mark-porath/'),
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:m.rath.oh@gmail.com'),
                    html.A(html.I(className='fab fa-github-square mr-1'),
                           href='https://github.com/m-rath'),


                    html.Span('Fadil Shaikh', className='mr-2'),
                    html.A(html.I(className='fab fa-linkedin mr-1'),
                           href='www.linkedin.com/in/fadil-s-11544df'),
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:fscoder12@gmail.com'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/scoding2'),


                    html.Span('Youssef Al-Yakoob', className='mr-2'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/youssefalyakoob/'),
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:yalyakoob@gmail.com'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/yalyakoob'),


                    html.Span('Zack Rock', className='mr-2'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/zacharycrock/'),
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:crkosmos@gmail.com'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/ZacharyRock'),

                ],

                className='lead'

            ),

        )

    )
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(),
    footer
])


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/Predictions':
        return predictions.layout
    elif pathname == '/Insights':
        return insights.layout
    elif pathname == '/Process':
        return process.layout
    # elif pathname == '/Result':
    #     return Result.layout
    else:
        return dcc.Markdown('## Page not found')


# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    app.run_server(debug=True)