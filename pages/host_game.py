import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table
import pandas as pd
from datetime import date

name_input = dbc.FormGroup(
    [
        dbc.Label("Name of the game", html_for="host_game_name"),
        dcc.Dropdown(
            id='demo-dropdown',
            options=[
                {'label': 'BANANAGRAMS', 'value': 1},
                {'label': 'EXPLODING KITTENS', 'value': 2},
                {'label': 'CARCASSONNE', 'value': 3},
                {'label': 'CODENAMES', 'value': 4},
                {'label': 'SETTLERS OF CATAN', 'value': 5},
                {'label': 'UNO', 'value': 6},
                {'label': 'HANABI', 'value': 7},
                {'label': 'DOBBLE', 'value': 8},
                {'label': 'RISK', 'value': 9},
                {'label': 'CARDS AGAINST HUMANITY', 'value': 10},
                {'label': 'DOMINO', 'value': 11},
                {'label': 'CHESS', 'value': 12},
            ],
        ),
        html.Div(id='dd-output-container')
    ]
)

when_input = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Date and Time", html_for="host_game_when", ),
                dbc.Input(
                    type="datetime-local",
                    id="host_game_time",
                ),
            ],
        )
    ],
)

where_input = dbc.FormGroup(
    [
        dbc.Label("Where will it be?", html_for="host_game_where"),
        dcc.Dropdown(
            id='demo-dropdown-2',
            options=[
                {'label': 'Cantine CROUS', 'value': 1},
                {'label': 'PUIO', 'value': 2},
                {'label': 'Library', 'value': 3},
                {'label': 'Dorm A', 'value': 4},
                {'label': 'Dorm B', 'value': 5},
            ],
            value=2
        ),
        html.Div(id='dd-output-container-2')
    ]
)

players_input = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("How many additional players do you need?", html_for="host_game_players", ),
                dbc.Input(
                    type="number",
                    id="host_game_players",
                ),
            ],
        )
    ],
)

image_input = dbc.FormGroup(
    [
        dbc.Label("Upload a selfie for everyone to recognize you :)", html_for="host_game_image"),
        dbc.Input(
            type="file",
            id="host_game_image",
            placeholder="Select an image",
        ),
    ]
)

layout = html.Div([

    dbc.Navbar(
        [
            dbc.Col(
                dbc.Row(
                    html.A(
                        html.B(
                            dbc.NavbarBrand("<"),
                            className="padding-small"
                        ),
                        href="/join_host_game",
                    ),
                    justify="center"
                ),
                width="auto"
            ),
            dbc.Col(
                dbc.Row(
                    dbc.NavbarBrand("Host a Game"),
                    justify="center"
                )
            ),
            dbc.Col(
                dbc.Row(
                    html.B(
                        html.A(
                            html.I(className="fa fa-user fa-lg", style= {'color':'white'}),
                            # href="/",
                        )
                    ),
                    justify="center"
                ),
                width="auto"
            ),
        ],
        color="dark",
        dark=True,
    ),

    dbc.Row(
        children=[
            dbc.Col(
                width=1
            ),
            dbc.Col(
                children=[

                    html.Br(),

                    dbc.Form([
                        name_input, 
                        when_input, 
                        where_input,
                        players_input,
                        image_input, 
                        html.Br(),
                        dbc.Button(
                            "Publish game session", 
                            id="host_button",
                            n_clicks=0, 
                            color="primary",
                            block=True,
                            href="/join_host_game"
                        ), 
                    ]),
                ]
            ),
            dbc.Col(
                width=1
            ),
        ]
    ),
])
