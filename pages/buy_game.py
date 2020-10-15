import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table
import pandas as pd

layout = html.Div([

    dbc.Navbar(
        [
            dbc.Col(
                dbc.Row(
                    html.B(
                        html.A(
                            dbc.NavbarBrand("<"),
                            # html.I(className="fa fa-arrow-left"),
                            href="/buy_sell_rent",
                        )
                    ),
                    justify="center"
                ),
                width="auto"
            ),
            dbc.Col(
                dbc.Row(
                    # html.A(
                    dbc.NavbarBrand("Buy a Game"),
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
                    dbc.Row(
                        dbc.Card(
                            [
                                dbc.CardImg(src="/assets/images/catan.jpg", top=True),
                                dbc.CardBody(
                                    [
                                        html.H3("Catan", className="card-title"),
                                        html.H4("20€", className="card-title"),
                                        html.P(
                                            "Almost new. No pieces are missing :)",
                                            # "make up the bulk of the card's content.",
                                            className="card-text",
                                        ),

                                        html.Br(),

                                        dbc.Button("Contact the seller", color="primary", block=True,
                                                   href="/contact_seller"),
                                    ]
                                ),
                            ],
                            # style={"width": "18rem"},
                        ),
                    justify="center"
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
