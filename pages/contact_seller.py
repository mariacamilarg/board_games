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
                            href="/buy_game", id="link_seller"
                        )
                    ),
                    justify="center"
                ),
                width="auto"
            ),
            dbc.Col(
                dbc.Row(
                    # html.A(
                    dbc.NavbarBrand("Contact the seller"),
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

                    dbc.Collapse(
                        children=[
                            html.Br(),

                            html.Div(
                                [
                                    html.Div([
                                        html.H5("Let Camille how to pay and collect the game")]),

                                ],
                            ),

                        ]
                        , id="buy_m1"
                    ),

                    dbc.Collapse(
                        children=[
                            html.Br(),

                            html.Div(
                                [
                                    html.Div([html.H5("by Abby"),
                                              html.H5(
                                                  "Hi Camille, I’d love to play as soon as possible.")]),

                                ], className="message align-message-right",
                            ),
                        ]
                        , id="buy_m2"
                    ),

                    dbc.Collapse(
                        children=[
                            html.Br(),

                            html.Div(
                                [
                                    html.Div([html.H5("by Camille"),
                                              html.H5(
                                                  "Sure, no problem! Do you live in Orsay? ")]),

                                ], className="message",
                            ),

                        ]
                        , id="buy_m3"
                    ),

                    dbc.Collapse(
                        children=[
                            html.Br(),

                            html.Div(
                                [
                                    html.Div([html.H5("by Abby"),
                                              html.H5(
                                                  "I live in Paris, so it's not a problem for me to come")]),

                                ], className="message align-message-right",
                            ),

                        ]
                        , id="buy_m4"
                    ),

                    dbc.Collapse(
                        children=[
                            html.Br(),

                            html.Div(
                                [
                                    html.Div([html.H5("by Camille"),
                                              html.H5("Perfect. We could meet Monday or Tuesday morning")]),

                                ], className="message",
                            ),

                        ]
                        , id="buy_m5"
                    ),

                    dbc.Collapse(
                        children=[
                            html.Br(),

                            html.Div(
                                [
                                    html.Div([html.H5("by Abby"),
                                              html.H5(
                                                  "I'm good for Monday morning 😊")]),

                                ], className="message align-message-right",
                            ),

                        ]
                        , id="buy_m6"
                    ),

                    dbc.Collapse(
                        children=[
                            html.Br(),

                            html.Div(
                                [
                                    html.Div([html.H5("by Camille"),
                                              html.H5("Ok. See you on Monday")]),

                                ], className="message",
                            ),

                        ]
                        , id="buy_m7"
                    ),

                    dcc.Interval(id='interval3', interval=3 * 1000, n_intervals=0),
                    html.H5(id='label3', children='', className="white")

                ]
            ),

            dbc.Col(
                width=1
            ),
        ]
    ),

])
