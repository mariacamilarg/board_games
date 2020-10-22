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
                            #href="/join_game?id=1", 
                            id="join_game_link_request"
                        )
                    ),
                    justify="center"
                ),
                width="auto"
            ),
            dbc.Col(
                dbc.Row(
                    dbc.NavbarBrand("Request to join"),
                    justify="center"
                )
            ),
            dbc.Col(
                dbc.Row(
                    html.B(
                        html.A(
                            html.I(className="fa fa-user fa-lg", style= {'color':'white'}),
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

                    dbc.Collapse(
                        html.Div(
                            "", #"You are requesting to join EXPLODING KITTENS for Today @ 12:30pm",
                            id="request_info",
                        ),
                        is_open=True
                    ),

                    html.Br(),

                    dbc.Collapse(
                        html.Div(
                            [
                                html.H5("by Abby"),
                                html.H5(
                                    "Hi Luis, I’d like to join your game!"
                                )
                            ], 
                            className="message align-message-right",
                        ),
                        is_open=True
                    ),

                    html.Br(),

                    dbc.Row(
                        children=[
                            dbc.Button(
                                "Add a +1",
                                color="success",
                                className="mr-1"
                            ),
                            dbc.Col(width=1),
                        ],
                        justify="end"
                    ),

                    html.Br(),

                    dbc.Collapse(
                        children=[
                            html.Div(
                                [
                                    html.H5("by Luis"),
                                    html.H5("Sure, see you there!")
                                ], 
                                className="message",
                            ),
                            html.Br(),  
                            "Luis has accepted your request, here are the rest of the players:",
                            dbc.Row(
                                children=[
                                    dbc.Col(
                                        dbc.CardImg(
                                            src="/assets/images/person1.png", 
                                        ),
                                    ),
                                    dbc.Col(
                                        dbc.CardImg(
                                            src="/assets/images/person22.png", 
                                        ),
                                    ),
                                    dbc.Col(
                                        dbc.CardImg(
                                            src="/assets/images/person3.png", 
                                        ),
                                    ),
                                ]
                            ),
                            html.Br(),  
                            "Please upload a selfie so others can recognize you :)",
                            dbc.Row(
                                children=[
                                    dcc.Upload(
                                        dbc.Button(
                                            "Take a selfie 📸",
                                            color="success",
                                            className="mr-1"
                                        ),
                                        id='upload-image',
                                    ),
                                    dbc.Col(width=1),
                                ],
                                justify="end"
                            ),
                        ],
                        id="reply_join",
                        is_open=False
                    ),

                    html.Br(),

                    dbc.Collapse(
                        children=[
                            "Wonderful Abby, enjoy your game!",
                            dbc.Row(
                                dbc.Col(
                                    dbc.CardImg(
                                        src="/assets/images/person1.png", 
                                        id="output-image-upload"
                                    ),
                                    width=5
                                ),
                                justify="center"
                            ),
                            html.Br(),
                            html.Div(
                                [
                                    html.H5("by Abby"),
                                    html.H5(
                                        "Thank Luis, see you!"
                                    )
                                ], 
                                className="message align-message-right",
                            ),
                            html.Br(),
                        ],
                        id="request_result",
                    ),

                    dcc.Interval(
                        id='interval_request', 
                        interval=3 * 1000, 
                        n_intervals=0
                    ),
                ]
            ),

            dbc.Col(
                width=1
            ),
        ]
    ),

])
