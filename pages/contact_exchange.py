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
                            href="/see_exchange_game", id="link_exchanger"
                        )
                    ),
                    justify="center"
                ),
                width="auto"
            ),
            dbc.Col(
                dbc.Row(
                    # html.A(
                    dbc.NavbarBrand("Contact the exchanger"),
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

                    dbc.Collapse(
                        children=[
                            html.Br(),

                                html.Div(
                                    [
                                        html.Div([
                                        html.H5("Let Camille know when to exchange your games")]),


                                    ],
                                ),

                        ]
                        , id="exchange_m1"
                    ),

                    dbc.Collapse(
                        children=[
                            html.Br(),

                                html.Div(
                                    [
                                        html.Div([html.H5("by Abby"),
                                                  html.H5("Hi Camille, I'd like to meet at the end of this week. Is that possible?")]),


                                    ], className="message align-message-right",
                                ),
                        ]
                        , id="exchange_m2"
                    ),

dbc.Collapse(
                        children=[
                            html.Br(),

                                html.Div(
                                    [
                                        html.Div([html.H5("by Camille"),
                                                  html.H5("Sure! How about near the Eiffel tower?")]),


                                    ], className="message",
                                ),

                        ]
                        , id="exchange_m3"
                    ),

dbc.Collapse(
                        children=[
                            html.Br(),

                                html.Div(
                                    [
                                        html.Div([html.H5("by Abby"),
                                                  html.H5("Perfect, we could do the exchange there.")]),


                                    ], className="message align-message-right",
                                ),

                        ]
                        , id="exchange_m4"
                    ),

dbc.Collapse(
                        children=[
                            html.Br(),

                                html.Div(
                                    [
                                        html.Div([html.H5("by Camille"),
                                                  html.H5("So, Friday afternoon?")]),


                                    ], className="message",
                                ),

                        ]
                        , id="exchange_m5"
                    ),

dbc.Collapse(
                        children=[
                            html.Br(),

                                html.Div(
                                    [
                                        html.Div([html.H5("by Abby"),
                                                  html.H5("Yes! Friday is good 😊")]),


                                    ], className="message align-message-right",
                                ),

                        ]
                        , id="exchange_m6"
                    ),

dbc.Collapse(
                        children=[
                            html.Br(),

                                html.Div(
                                    [
                                        html.Div([html.H5("by Camille"),
                                                  html.H5("Ok. See ya ")]),

                                    ], className="message",
                                ),

                        ]
                        , id="exchange_m7"
                    ),

                    dcc.Interval(id='interval1', interval=3 * 1000, n_intervals=0),
                    html.H5(id='label1', children='', className="white")

                ]
            ),

            dbc.Col(
                width=1
            ),
        ]
    ),

])
