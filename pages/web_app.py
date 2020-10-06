import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Row(
        children=[
            dbc.Col(
                width=1
            ),
            dbc.Col(
                children=[
                    html.Br(),
                    dbc.Row(
                        html.H1("What do you want to do?")
                    ),

                    html.Br(),
                    html.Br(),

                    dbc.Row(
                        html.A(
                            dbc.Button(
                                'JOIN A GAME', 
                                id="join_game_button",
                                color="success", 
                                className="mr-1",
                            ),
                            href="/join_game",
                        ),
                        justify='center'
                    ),

                    html.Br(),

                    dbc.Row(
                        html.A(
                            dbc.Button(
                                'BORROW A GAME NOW', 
                                id="borrow_game_now_button",
                                color="success", 
                                className="mr-1",
                            ),
                            href="/join_game",
                        ),
                        justify='center'
                    ),

                    html.Br(),

                    dbc.Row(
                        html.A(
                            dbc.Button(
                                'BORROW A GAME LATER', 
                                id="borrow_game_later_button",
                                color="success", 
                                className="mr-1",
                            ),
                            href="/join_game",
                        ),
                        justify='center'
                    ),

                    html.Br(),

                    dbc.Row(
                        html.A(
                            dbc.Button(
                                'SHARE YOUR GAMES', 
                                id="share_games_button",
                                color="success", 
                                className="mr-1",
                            ),
                            href="/join_game",
                        ),
                        justify='center'
                    ),

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
