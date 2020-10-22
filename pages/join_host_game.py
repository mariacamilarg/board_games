import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table
import pandas as pd

from widgets import campus_map


layout = html.Div([

    dbc.Navbar(
        [
            dbc.Col(
                dbc.Row(
                    html.A(
                        html.B(
                            dbc.NavbarBrand("<"),
                            className="padding-small"
                        ),
                        href="/",
                    ),
                    justify="center"
                ),
                width="auto"
            ),
            dbc.Col(
                dbc.Row(
                    dbc.NavbarBrand("Join/Host a Game"),
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
                    
                    #title
                    dbc.Row(
                        html.H2("Happening around you:"),
                    ),

                    dbc.Row(
                        dcc.Graph(
                            id='campus_map',
                            config={
                                'displayModeBar': False, 
                                'scrollZoom': True
                            },
                            style={
                                'background': '#000000', 
                                'height': '35vh',
                                'width': '90vw'
                            },
                        ),
                    ),

                    html.Br(),

                    dbc.Row(
                        children=[
                            dbc.Col(
                                "In the next: ",
                                width=3
                            ),
                            dbc.Col(
                                dcc.Slider(
                                    min=1,
                                    max=36,
                                    step=None,
                                    marks={
                                        1: '1h',
                                        6: '6h',
                                        12: '12h',
                                        24: '1d',
                                        36: '2d'
                                    },
                                    value=6,
                                    id="slider_join_game",
                                )
                            ),
                            dbc.Col(
                                dbc.Button(
                                    html.I(
                                        className='fa fa-filter fa-lg',
                                    ),
                                    id='filter-button',
                                ),
                                width=2
                            ),
                            dbc.Modal(
                                [
                                    dbc.ModalHeader("Filter game sessions"),
                                    dbc.ModalBody(
                                        children=[
                                            "Categories",
                                            html.Br(),
                                            dcc.Dropdown(
                                                options=[
                                                    {'label': 'cards', 'value': 'cards'},
                                                    {'label': 'strategy', 'value': 'strategy'},
                                                    {'label': 'words', 'value': 'words'}
                                                ],
                                                value=['cards', 'strategy', 'words'],
                                                multi=True
                                            ),
                                            html.Br(),
                                            "Duration range (in minutes)",
                                            html.Br(),
                                            dcc.RangeSlider(
                                                id='my-range-slider',
                                                min=0,
                                                max=120,
                                                step=30,
                                                value=[30, 90],
                                                marks={
                                                    0: {'label': '0m'},
                                                    30: {'label': '30m'},
                                                    60: {'label': '60m'},
                                                    90: {'label': '90m'},
                                                    120: {'label': '120m'}
                                                }
                                            ),
                                            html.Br(),
                                            "Difficulty (1 = easy, 5 = hard)",
                                            html.Br(),
                                            dcc.Checklist(
                                                options=[
                                                    {'label': '. 1 .', 'value': 1},
                                                    {'label': '. 2 .', 'value': 2},
                                                    {'label': '. 3 .', 'value': 3},
                                                    {'label': '. 4 .', 'value': 4},
                                                    {'label': '. 5 .', 'value': 5},
                                                ],
                                                value=[1,2,3,4],
                                                labelStyle={'display': 'inline-block'}
                                            ),
                                            html.Br(),
                                            "Number of players (maximum)",
                                            html.Br(),
                                            dcc.RangeSlider(
                                                id='my-range-slider',
                                                min=1,
                                                max=12,
                                                step=1,
                                                value=[4, 8],
                                                marks={
                                                    4: {'label': '4p'},
                                                    8: {'label': '8p'},
                                                    12: {'label': '12p'},
                                                    1: {'label': '1p'},
                                                    2: {'label': '2p'},
                                                    3: {'label': '3p'},
                                                    5: {'label': '5p'},
                                                    6: {'label': '6p'},
                                                    7: {'label': '7p'},
                                                    9: {'label': '9p'},
                                                    10: {'label': '10p'},
                                                    11: {'label': '11p'},
                                                }
                                            ),
                                        ]
                                    ),
                                    dbc.ModalFooter(
                                        dbc.Button("Filter", id="close-2", className="ml-auto")
                                    ),
                                ],
                                size="sm",
                                id="modal-2",
                            ),
                        ]
                    ),

                    html.Br(),

                    # List of games

                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.CardImg(src="/assets/images/plus.png"),
                                    width=3
                                ),
                                dbc.Col(
                                    html.H5(["HOST A NEW GAME !"]),
                                    align="center"
                                ),
                            ],
                        ),
                        href="/host_game"
                    ),

                    html.Br(),

                    html.Div(
                        id="list_games_div",
                    ),

                    # html.A(
                    #     dbc.Row(
                    #         [
                    #             dbc.Col(
                    #                 dbc.CardImg(src="/assets/images/bananagrams.jpg", id="img1"), 
                    #                 width=2
                    #             ),
                    #             dbc.Col(
                    #                 width=1
                    #             ),
                    #             dbc.Col(
                    #                 children=[
                    #                     dbc.Row(
                    #                         children=[
                    #                             "Today"
                    #                         ],
                    #                     ),
                    #                     dbc.Row(
                    #                         children=[
                    #                             "@ 12:30pm",
                    #                         ],
                    #                     ),
                    #                 ],
                    #                 width=4
                    #             ),
                    #             dbc.Col(
                    #                 children=[
                    #                     dbc.Row(
                    #                         children=[
                    #                             "Bananagrams",
                    #                         ],
                    #                     ),
                    #                     dbc.Row(
                    #                         children=[
                    #                             html.I(className='fa fa-clock-o fa-sm'),
                    #                             " 1h30 . . . ",
                    #                             html.I(className='fa fa-users fa-sm'),
                    #                             " 3/5",
                    #                         ],
                    #                     ),
                    #                 ]
                    #             ),
                    #         ],
                    #     ),
                    #     href="/host_game?id=1"
                    # ),

                    # html.Br(),

                    # html.A(
                    #     dbc.Row(
                    #         [
                    #             dbc.Col(
                    #                 dbc.CardImg(src="/assets/images/codenames.jpg", id="img2"), 
                    #                 width=2
                    #             ),
                    #             dbc.Col(
                    #                 width=1
                    #             ),
                    #             dbc.Col(
                    #                 children=[
                    #                     dbc.Row(
                    #                         children=[
                    #                             "Today"
                    #                         ],
                    #                     ),
                    #                     dbc.Row(
                    #                         children=[
                    #                             "@ 5:00pm",
                    #                         ],
                    #                     ),
                    #                 ],
                    #                 width=4
                    #             ),
                    #             dbc.Col(
                    #                 children=[
                    #                     dbc.Row(
                    #                         children=[
                    #                             "Codenames",
                    #                         ],
                    #                     ),
                    #                     dbc.Row(
                    #                         children=[
                    #                             html.I(className='fa fa-clock-o fa-sm'),
                    #                             " 1h00 . . . ",
                    #                             html.I(className='fa fa-users fa-sm'),
                    #                             " 7/10",
                    #                         ],
                    #                     ),
                    #                 ]
                    #             ),
                    #         ],
                    #     ),
                    #     href="/host_game?id=2"
                    # ),

                    # html.Br(),

                    # html.A(
                    #     dbc.Row(
                    #         [
                    #             dbc.Col(
                    #                 dbc.CardImg(src="/assets/images/catan.jpg", id="img3"), 
                    #                 width=2
                    #             ),
                    #             dbc.Col(
                    #                 width=1
                    #             ),
                    #             dbc.Col(
                    #                 children=[
                    #                     dbc.Row(
                    #                         children=[
                    #                             "Tomorrow"
                    #                         ],
                    #                     ),
                    #                     dbc.Row(
                    #                         children=[
                    #                             "@ 10:00am",
                    #                         ],
                    #                     ),
                    #                 ],
                    #                 width=4
                    #             ),
                    #             dbc.Col(
                    #                 children=[
                    #                     dbc.Row(
                    #                         children=[
                    #                             "Settlers of Catan",
                    #                         ],
                    #                     ),
                    #                     dbc.Row(
                    #                         children=[
                    #                             html.I(className='fa fa-clock-o fa-sm'),
                    #                             " 1h30 . . . ",
                    #                             html.I(className='fa fa-users fa-sm'),
                    #                             " 3/6",
                    #                         ],
                    #                     ),
                    #                 ]
                    #             ),
                    #         ],
                    #     ),
                    #     href="/host_game?id=3"
                    # ),
                    #
                    # dbc.Row(
                    #     dash_table.DataTable(
                    #         id='join_games_table',
                    #         style_header = {
                    #             'display': 'none'
                    #         },
                    #         style_table={
                    #             'width': '100%',
                    #             'minWidth': '100%',
                    #         },
                    #         # css=[{
                    #         #     "selector": "table", 
                    #         #     "rule": "width: 100%;"
                    #         # }],
                    #         style_cell={
                    #             'textAlign': 'center',
                    #         },
                    #         #page_size=10,
                    #     ),
                    #     justify="center"
                    # ),
                ]
            ),
            dbc.Col(
                width=1
            ),
        ]
    ),
])

