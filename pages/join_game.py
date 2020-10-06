import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table
import pandas as pd

layout = html.Div([

    dbc.Row(
        children=[
            dbc.Col(
                width=1
            ),
            dbc.Col(
                children=[

                    html.Br(),
                    
                    #title
                    dbc.Row(
                        html.H2("List of games in DB"),
                    ),

                    html.Br(),
                    html.Br(),

                    dbc.Row(
                        children=[
                            dbc.Col(
                                dash_table.DataTable(
                                    id='all_games_table',
                                    style_cell={
                                        'textAlign': 'left',
                                    },
                                )
                            )
                        ]
                    ),

                    html.Br(),
                ]
            ),
            dbc.Col(
                width=1
            ),
        ]
    ),
])

