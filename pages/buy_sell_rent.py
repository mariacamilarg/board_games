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

# dbc.Row(
#     dbc.Col(
#         dbc.CardImg(src="/assets/images/catan.jpg", top=True),
#     ),
#     dbc.Col(
#         dbc.Card(
#             [
#                 dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
#                 dbc.CardBody(
#                     [
#                         html.H4("Card title", className="card-title"),
#                         html.P(
#                             "Some quick example text to build on the card title and "
#                             "make up the bulk of the card's content.",
#                             className="card-text",
#                         ),
#                         dbc.Button("Go somewhere", color="primary"),
#                     ]
#                 ),
#             ],
#             style={"width": "18rem"},
#         )
#     )
# )


layout = html.Div([

    dbc.Navbar(
        [
            dbc.Col(
                dbc.Row(
                    html.B(
                        html.A(
                            dbc.NavbarBrand("<"),
                            # html.I(className="fa fa-arrow-left"),
                            href="/",
                        )
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
                        html.H3("BUY SELL RENT EXCHANGE")
                        , justify="center"
                    ),

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

                    html.Br(),

                    # title
                    dbc.Row(
                        dbc.ButtonGroup(
                            [dbc.Button("Buy", color="primary", active="True"),
                             dbc.Button("Rent", color="success"),
                             dbc.Button("Sell", color="warning"),
                             dbc.Button("Exchange", color="danger")]
                            , className="w-100",
                        )
                        , justify="center"
                    ),

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

                    html.Br(),

                    # card
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
                                            html.H3(["Catan"]),
                                            html.H4(["20€"]),
                                        ]),
                                    # justify="center", className="px-1"
                                # ),
                            ),
                        ],
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
