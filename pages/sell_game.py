import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table
import pandas as pd

name_input = dbc.FormGroup(
    [
        dbc.Label("Name of the game", html_for="sell_game_name"),
        dbc.Input(id='sell_game_name', type='text', placeholder="Enter the name of the game", ),

    ]
)

price_input = dbc.FormGroup(
    [
        dbc.Label("Price in euro", html_for="sell_game_price"),
        dbc.Input(
            type="number",
            id="sell_game_price",
            placeholder="Enter the price",
        ),
    ]
)

image_input = dbc.FormGroup(
    [
        dbc.Label("Image", html_for="sell_game_img"),
        dbc.Input(
            type="file",
            id="sell_game_img",
            placeholder="Select an image",
        ),
    ]
)


desc_input = dbc.FormGroup(
    [
        dbc.Label("Description ", html_for="sell_game_desc"),
        dbc.Input(type="text", id="sell_game_desc", placeholder="Enter a short description", ),

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
                    dbc.NavbarBrand("Sell a Game"),
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

                    dbc.Form([name_input, price_input, image_input, desc_input, html.Br(),
                              dbc.Button("Sell the game", id="sell_button", n_clicks=0, color="primary", block=True, ), ]),

                    html.Div(id='container-button-basic',
                             children='Enter a value and press submit'),
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
