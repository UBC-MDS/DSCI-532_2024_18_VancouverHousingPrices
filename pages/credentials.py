import sys
sys.path.append('../')

from dash import html
import dash_bootstrap_components as dbc
import menu
import dash
from dash import dcc
from dash.dependencies import Input, Output, State
from app import app
from dash import Dash, html, dcc, dash_table, ctx
from dash import callback_context
import numpy as np

from assets.texts import jenny

import plotly.graph_objects as go

import pandas as pd

fig = go.Figure()

dash.register_page(__name__, path="/", title="Credentials")

def make_card(photo, name, description):
      card = dbc.Card([
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src=f"assets/{photo}.png",
                        className="img-fluid rounded-start",
                        style={'height':'150px', 
                               'width':'150px',
                               "text-align": "center",
                               "top": 0, "left": 50,
                               "align":"center",}
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4(f"{name}", className="card-title"),
                            html.P(
                                description
                            ),                            
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        ),
    ],
    color="primary", outline=True,
    className="mb-3",
    style={"maxWidth": "700px", "height": "150px"},
      )
      return card

maindiv = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H4("Meet the Team"), style={'display': 'inline-block',
                                                 "text-align": "left",
                                                 "color": "#d85e30",
                                                #  "font-family": "Arial, sans-serif",
                                                 "font-weight": "italic"},
                                                 align="top", width=3
            ),
            dbc.Col([
                  html.P(
                        "We are group of data science students enrolled in Master of Data Science program."
                  ),
                  make_card(jenny[1], jenny[0], jenny[2]),
                  make_card(jenny[1], jenny[0], jenny[2]),
                  make_card(jenny[1], jenny[0], jenny[2]),
                  make_card(jenny[1], jenny[0], jenny[2])
        ])
        ]),
         html.Hr(),
         dbc.Row([
            dbc.Col(
                html.H4("Inspiration"), style={'display': 'inline-block',
                                                 "text-align": "left",
                                                 "color": "#d85e30",
                                                #  "font-family": "Arial, sans-serif",
                                                 "font-weight": "bold"},
                                                 align="top", width=3
            ),
            dbc.Col([
                  html.P(
                        "We are group of data science students enrolled in Master of Data Science program."
                  ),
                  html.P(
                        "Latest Upate: --/--/--", style={'display': 'inline-block',
                                                         "text-align": "left",
                                                         "color": "#000000",
                                                #  "font-family": "Arial, sans-serif",
                                                "font-weight": "bold"}
                  )
        ])
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                html.H4("References"), style={'display': 'inline-block',
                                                 "text-align": "left",
                                                 "color": "#d85e30",
                                                #  "font-family": "Arial, sans-serif",
                                                 "font-weight": "bold"},
                                                 align="top", width=3
            ),
            dbc.Col([
                  html.Ul([
                        html.Li("This is where the credentials go"),
                        html.Li("Okay Sure")
                  ], id='credential-list')

        ])
        ])
    ]),

])


layout = html.Div(children=[
    menu.dropdown_menu,

    dbc.Row([
        dbc.Col(maindiv)  
    ])
])