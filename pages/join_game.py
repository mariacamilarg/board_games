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
                            href="/join_host_game",
                        )
                    ),
                    justify="center"
                ),
                width="auto"
            ),
            dbc.Col(
                dbc.Row(
                    dbc.NavbarBrand("Join a Game"),
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

                    # img
                    dbc.Row(
                        dbc.CardImg(
                            #src="/assets/images/bananagrams.jpg", 
                            id="join-img"
                        ),
                        justify="center"
                    ),

                    # title
                    dbc.Row(
                        html.H3(
                            "",#"BANANAGRAMS",
                            id="join-name"
                        ),
                        justify="center"
                    ),

                    html.Br(),

                    dbc.Row(
                        "",#"Today @ 12:30pm",
                        id="join-when",
                        justify="center"
                    ),
                    dbc.Row(
                        children=[
                            ""
                            # html.I(className='fa fa-clock-o fa-sm'),
                            # " 1h30 . .",
                            # html.I(className='fa fa-users fa-sm'),
                            # " 3/5 . .",
                            # html.I(className='fa fa-signal fa-sm'),
                            # " 1/5"
                        ],
                        id="join-details",
                        justify="center"
                    ),
                    dbc.Row(
                        "", #"Categories: words",
                        id="join-category",
                        justify="center"
                    ),

                    html.Br(),

                    dbc.Row(
                        dbc.Button(
                            html.H3("Share with friend"), 
                            id="share_button",
                            color="warning", 
                            size="lg",
                            block=True,
                            #href="/share_join",
                        ),
                    ),

                    html.Br(),

                    dbc.Row(
                        dbc.Button(
                            html.H3("Request to join"), 
                            id="request_button",
                            color="info", 
                            size="lg",
                            block=True,
                            #href="/request_join?id=1",
                        ),
                    ),
                ]
            ),
            dbc.Col(
                width=1
            ),
        ]
    ),




])
