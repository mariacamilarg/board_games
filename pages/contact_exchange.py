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
                                        html.H5("Let Camille know when and for how long you want to rent her game")]),


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
                                                  html.H5("Hi Camille, I’d love to rent your game next Tuesday afternoon. Is that possible?")]),


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
                                                  html.H5("Sure! Do you live in Orsay? You could pick it up Tuesday morning")]),


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
                                                  html.H5("I live in Paris… 😕 Will you be at uni on Monday or Tuesday? We could meet there")]),


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
                                                  html.H5("Yeah, I have a class Monday afternoon")]),


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
                                                  html.H5("Awesome! I’ll rent it from Monday afternoon to Tuesday then? We can meet after your lecture 😊")]),


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
                                                  html.H5("Ok. It’s at the Eiffel building. See you ")]),

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
