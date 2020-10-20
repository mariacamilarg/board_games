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
                    dbc.NavbarBrand("Buy - Sell - Rent - Exchange", id="page_title"),
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
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="img1")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["BUY Catan"], id="name1"),
                                                    html.H4(["20€"], id="price1"),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/buy_game?id=1"
                            ),

                            html.Br(),

                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="img2")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["BUY Catan"], id="name2"),
                                                    html.H4(["20€"], id="price2"),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/buy_game?id=2"
                            ),

                            html.Br(),
                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="img3")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["BUY Catan"], id="name3"),
                                                    html.H4(["20€"], id="price3"),
                                                ]),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/buy_game?id=3",
                            ),

                            html.Br(),
                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="img4")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["BUY Catan"], id="name4"),
                                                    html.H4(["20€"], id="price4"),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/buy_game?id=4"
                            ),

                            html.Br(),
                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="img5")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["BUY Catan"], id="name5"),
                                                    html.H4(["20€"], id="price5"),
                                                ]),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/buy_game?id=5",
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
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="rent_img1")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["RENT Catan"], id="rent_name1"),
                                                    html.H4(["20€"], id="rent_price1"),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/rent_game?id=1"
                            ),

                            html.Br(),

                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="rent_img2")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["RENT Catan"], id="rent_name2"),
                                                    html.H4(["20€"], id="rent_price2"),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/rent_game?id=2"
                            ),

                            html.Br(),
                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="rent_img3")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["RENT Catan"], id="rent_name3"),
                                                    html.H4(["20€"], id="rent_price3"),
                                                ]),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/rent_game?id=3",
                            ),

                            html.Br(),
                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="rent_img4")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["RENT Catan"], id="rent_name4"),
                                                    html.H4(["20€"], id="rent_price4"),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/rent_game?id=4"
                            ),

                            html.Br(),
                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="rent_img5")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["RENT Catan"], id="rent_name5"),
                                                    html.H4(["2€"], id="rent_price5"),
                                                ]),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/rent_game?id=5",
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
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="exchange_img1")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["EXCHANGE Catan"], id="exchange_wanted1"),
                                                    html.H4(["CARCASSONNE"], id="exchange_offered1"),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/see_exchange_game?id=1"
                            ),

                            html.Br(),

                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="exchange_img2")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["EXCHANGE Catan"], id="exchange_wanted2"),
                                                    html.H4(["CARCASSONNE"], id="exchange_offered2"),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/see_exchange_game?id=2"
                            ),

                            html.Br(),
                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="exchange_img3")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["EXCHANGE Catan"], id="exchange_wanted3"),
                                                    html.H4(["CARCASSONNE"], id="exchange_offered3"),
                                                ]),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/see_exchange_game?id=3",
                            ),

                            html.Br(),
                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="exchange_img4")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["EXCHANGE Catan"], id="exchange_wanted4"),
                                                    html.H4(["CARCASSONNE"], id="exchange_offered4"),
                                                ]),
                                            # justify="center", className="px-1"
                                            # ),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/see_exchange_game?id=4"
                            ),

                            html.Br(),
                            # card ###############################
                            html.A(
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            # dbc.Row(
                                            dbc.CardImg(src="/assets/images/catan.jpg", id="exchange_img5")
                                            # ),
                                            , width=4
                                        ),
                                        dbc.Col(
                                            # dbc.Row(
                                            html.Div(
                                                [
                                                    html.H3(["EXCHANGE Catan"], id="exchange_wanted5"),
                                                    html.H4(["CARCASSONNE"], id="exchange_offered5"),
                                                ]),
                                            className="my-auto"
                                        ),
                                    ],
                                ),
                                href="/see_exchange_game?id=5",
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
