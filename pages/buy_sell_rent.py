import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table
import pandas as pd

card_content = [

    # dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

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
                        href="/",
                    ),
                    justify="center"
                ),
                width="auto"
            ),
            dbc.Col(
                dbc.Row(
                    # html.A(
                    dbc.NavbarBrand("Buy - Sell - Rent - Exchange"),
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

                    # title
                    # dbc.Row(
                    dbc.ButtonGroup(
                        [dbc.Button("Buy", color="primary", active="True", id="buy-button", ),
                         dbc.Button("Rent", color="success", id="rent-button", ),
                         dbc.Button("Exchange", color="warning", id="exchange-button", )]
                        , className="w-100",
                    ),
                    # , justify="center"
                    # ),

                    html.Br(),
                    html.Br(),
                ]
            ),
            dbc.Col(
                width=1
            ),
        ]
    ),

    dbc.Row(
        children=[
            dbc.Col(
                width=1
            ),

            dbc.Col(

                children=[

                    # BUY
                    dbc.Collapse(
                        children=[

                            html.Br(),

                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/plus.png", )
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["SELL A GAME"]),
                                                ]),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/sell_game"
                            ),

                            html.Br(),

                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", )
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["BUY Catan"]),
                                                    html.H4(["20€"]),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/buy_game"
                            ),

                            html.Br(),

                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", )
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["BUY Catan"]),
                                                    html.H4(["20€"]),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/buy_game"
                            ),

                            html.Br(),
                        ],
                        id="buy"
                    ),

                    # RENT
                    dbc.Collapse(
                        children=[
                            html.Br(),

                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/plus.png", )
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["RENT OUT A GAME"]),
                                                ]),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/rent_out_game"
                            ),

                            html.Br(),

                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", )
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["RENT Catan"]),
                                                    html.H4(["5€ per day"]),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/buy_game"
                            ),

                            html.Br(),
                        ],
                        id="rent"
                    ),

                    # EXCHANGE
                    dbc.Collapse(
                        children=[
                            html.Br(),

                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/plus.png", )
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["PROPOSE EXCHANGE"]),
                                                ]),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/exchange_game"
                            ),

                            html.Br(),
                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", )
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["WANTS Catan"]),
                                                    html.H4(["offers Carcassonne"]),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/buy_game"
                            ),

                            html.Br(),
                        ],
                        id="exchange"
                    ),

                ],
            ),

            dbc.Col(
                width=1
            ),
        ]
    ),

])
