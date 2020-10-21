import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table
import pandas as pd

name_input = dbc.FormGroup(
    [
        dbc.Label("Name of the game you want", html_for="exchange_game_name"),
        dbc.Input(id="exchange_game_name", type="text", placeholder="Enter the name of the game you want", ),

    ]
)

name2_input = dbc.FormGroup(
    [
        dbc.Label("Name of the game you offer", html_for="exchange_game_name2"),
        dbc.Input(id="exchange_game_name2", type="text",  placeholder="Enter the name of the game you offer", ),

    ]
)

image_input = dbc.FormGroup(
    [
        dbc.Label("Image", html_for="exchange_game_image"),
        dbc.Input(
            type="file",
            id="exchange_game_image",
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

                    dbc.Form([name_input, name2_input, image_input, html.Br(),
                              dbc.Button("Exchange the game", id="exchange_button", n_clicks=0, color="primary", block=True), ]),

                    html.Div(id='exchange_container-button-basic',
                             children=' '),
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
