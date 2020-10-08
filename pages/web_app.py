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
                            'BUY/RENT/EXCHANGE A GAME', 
                            id="borrow_game_now_button",
                            color="primary", 
                            block=True,
                            href="/join_game",
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
