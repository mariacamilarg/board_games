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
                        html.H3("What do you want to do?"),
                    justify="center"
                    ),

                    html.Br(),
                    html.Br(),

                    dbc.Row(
                        dbc.Button(
                            'JOIN A GAME OR CREATE YOUR OWN', 
                            id="join_game_button",
                            color="primary", 
                            block=True,
                            href="/join_game",
                        ),
                    ),

                    html.Br(),

                    dbc.Row(
                        dbc.Button(
                            'BUY, SELL, RENT OR EXCHANGE A GAME',
                            id="buy_sell_rent_button",
                            color="primary",
                            className="mr-1",
                            href="/buy_sell_rent",
                            block=True
                        ),
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
