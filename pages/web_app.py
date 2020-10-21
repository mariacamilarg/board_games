import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Navbar(
        [
            dbc.Col(
                dbc.Row(
                    html.H2(html.B("COME AND PLAY"), className="text-light"),
                    justify="center",
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
                    dbc.Row(
                        html.H3("What do you want to do?"),
                        justify="center"
                    ),

                    html.Br(),

                    dbc.Row(
                        dbc.Button(
                            html.H3(
                                children=[
                                    ".",
                                    html.Br(),
                                    html.Br(),
                                    "Join OR Host",
                                    html.Br(),
                                    html.Br(),
                                    "a game session",
                                    html.Br(),
                                    html.Br(),
                                    "."
                                ]
                            ), 
                            id="join_game_button",
                            color="warning", 
                            size="lg",
                            block=True,
                            href="/join_game",
                        ),
                    ),

                    html.Br(),

                    dbc.Row(
                        dbc.Button(
                            html.H3(
                                children=[
                                    ".",
                                    html.Br(),
                                    html.Br(),
                                    "Buy/Sell OR Rent",
                                    html.Br(),
                                    "OR Exchange",
                                    html.Br(),
                                    html.Br(),
                                    "a board game",
                                    html.Br(),
                                    html.Br(),
                                    ".",
                                ]
                            ),
                            id="buy_sell_rent_button",
                            color="info",
                            size="lg",
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
