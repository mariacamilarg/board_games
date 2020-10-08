import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([

dbc.Navbar(
        [
            dbc.Col(
                dbc.Row(
                    # html.A(
                    # dbc.CardImg(src="/assets/images/logo.png", ),

                    html.H1("COME AND PLAY", className="text-light"),
                    # href="/large",
                    # ),
                    justify="center",
                )
            ),

        ],
        color="blue",
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
                    dbc.Row(
                        html.H3("What do you want to do?")
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
                                'BUY, SELL, RENT OR EXCHANGE A GAME',
                                id="buy_sell_rent_button",
                                color="success", 
                                className="mr-1",
                            ),
                            href="/buy_sell_rent",
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
