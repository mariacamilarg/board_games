import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table
import pandas as pd

name_input = dbc.FormGroup(
    [
        dbc.Label("Name of the game you want", html_for="game_name"),
        dbc.Input(type="text", id="game_name", placeholder="Enter the name of the game you want", ),

    ]
)

name2_input = dbc.FormGroup(
    [
        dbc.Label("Name of the game you offer", html_for="game_name2"),
        dbc.Input(type="text", id="game_name2", placeholder="Enter the name of the game you offer", ),

    ]
)

image_input = dbc.FormGroup(
    [
        dbc.Label("Image", html_for="game_image"),
        dbc.Input(
            type="file",
            id="game_image",
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
                            # html.I(className="fa fa-arrow-left"),
                            className="padding-small"
                        ),
                        href="/buy_sell_rent",
                    ),
                    justify="center"
                ),
                width="auto"
            ),
            dbc.Col(
                dbc.Row(
                    # html.A(
                    dbc.NavbarBrand("Exchange a Game"),
                    # href="/large",
                    # ),
                    justify="center"
                )
            ),

            dbc.Col(
                dbc.Row(
                    html.B(
                        html.A(
                            dbc.NavbarBrand("👤"),
                            # html.I(className="fa fa-arrow-left"),
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

                    dbc.Form([name_input, name2_input, image_input, html.Br(),
                              dbc.Button("Exchange the game", color="primary", block=True), ]),
                    html.Br(),
                    html.Br(),
                ]
            ),
            dbc.Col(
                width=1
            ),
        ]
    ),
])
