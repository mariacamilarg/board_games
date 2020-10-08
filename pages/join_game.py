import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table
import pandas as pd

from widgets import campus_map


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
                        html.H2("Join a game"),
                    ),

                    dbc.Row(
                        dcc.Graph(
                            id='campus_map',
                            config={
                                'displayModeBar': False, 
                                'scrollZoom': True
                            },
                            style={
                                'background': '#000000', 
                                'height': '35vh',
                                'width': '90vw'
                            },
                        ),
                    ),

                    html.Br(),

                    dbc.Row(
                        children=[
                            dbc.Col(
                                "In the next: ",
                                width=3
                            ),
                            dbc.Col(
                                dcc.Slider(
                                    min=1,
                                    max=5,
                                    step=None,
                                    marks={
                                        1: '1h',
                                        2: '6h',
                                        3: '12h',
                                        4: '1d',
                                        5: '2d'
                                    },
                                    value=1,
                                    id="slider_join_game",
                                )
                            ),
                        ]
                    ),

                    html.Br(),

                    dbc.Row(
                        dbc.Button(
                            '+  Start a new game!', 
                            id="start_game_button",
                            color="success", 
                            block=True,
                            href="/start_game",
                        ),
                    ),

                    dbc.Row(
                        dash_table.DataTable(
                            id='join_games_table',
                            style_header = {
                                'display': 'none'
                            },
                            style_table={
                                'width': '100%',
                                'minWidth': '100%',
                            },
                            # css=[{
                            #     "selector": "table", 
                            #     "rule": "width: 100%;"
                            # }],
                            style_cell={
                                'textAlign': 'center',
                            },
                            #page_size=10,
                        ),
                        justify="center"
                    ),
                ]
            ),
            dbc.Col(
                width=1
            ),
        ]
    ),
])

