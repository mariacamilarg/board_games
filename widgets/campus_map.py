import plotly.graph_objs as go
import dash_html_components as html
import dash_bootstrap_components as dbc

MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoianVlc3BhZm84NyIsImEiOiJja2QwcWNiZ28wMTY0MnhwYmNqbDMxaGl0In0.SRdwqTCLquu35-2noY2tEQ'

def get_data(db, in_next_hours):

    df = db.get_join_games_df()

    # filter df
    df = df[ df["next_hours"] <= in_next_hours ]

    print(df)

    # map
    map_fig = render_map(df)

    # list
    games_list = []
    for i, game in df.iterrows():
        game_id = game["id"]
        a = html.A(dbc.Row(
            children=[
                dbc.Col(
                    dbc.CardImg(src=game["img"], id=f"img{game_id}"), 
                    width=2
                ),
                dbc.Col(
                    width=1
                ),
                dbc.Col(
                    children=[
                        dbc.Row(game["when"]),
                        dbc.Row(game["time"]),
                    ],
                    width=3
                ),
                dbc.Col(
                    children=[
                        dbc.Row(game["name"]),
                        dbc.Row(
                            children=[
                                html.I(className='fa fa-clock-o fa-sm'),
                                f"{game['time']} . .",
                                html.I(className='fa fa-users fa-sm'),
                                f"{game['current_players']}/{game['max_players']}",
                            ],
                        ),
                    ]
                ),
            ]),
            href=f"/join_game?id={game_id}"
        )

        games_list.append(a)
        games_list.append(html.Br())

    print(games_list)

    return map_fig, games_list


def render_map(df):
    # Create figure
    locations = [go.Scattermapbox(
        lon=df['longitude'],
        lat=df['latitude'],
        mode='markers',
        marker={'color': df['color'], 'size': 5 * df['factor']},
        unselected={'marker': {'opacity': 1}},
        selected={'marker': {'opacity': 0.5, 'size': 100}},
        hoverinfo='text',
        hovertext=df['name']
    )]

    # Return figure
    return {
        'data': locations,
        'layout': go.Layout(
            uirevision='foo',  # preserves state of figure/map after callback activated
            clickmode='event+select',
            hovermode='closest',
            hoverdistance=2,
            mapbox=dict(
                accesstoken=MAPBOX_ACCESS_TOKEN,
                bearing=0,
                style='outdoors',
                center=dict(
                    lat=48.705,
                    lon=2.17
                ),
                zoom=12,
            ),
            margin=dict(l=0, r=0, t=0, b=0)
        )
    }

def render_table(df):

    # buttons = []

    # for row in df.iterrows():
        
    #     dbc.Button(
    #         df['hov_txt'],
    #         id=f"start_game_button",
    #         color="success", 
    #         className="mr-1",

    #     ),
    #     dbc.Button("Open modal", id="open"),
    #     dbc.Modal(
    #         [
    #             dbc.ModalHeader("Header"),
    #             dbc.ModalBody("This is the content of the modal"),
    #             dbc.ModalFooter(
    #                 dbc.Button("Close", id="close", className="ml-auto")
    #             ),
    #         ],
    #         id="modal",
    #     ),


    #     b = html.A(
    #         dbc.Button(
    #             id="start_game_button",
    #             df['hov_txt'],
    #             color="success", 
    #             className="mr-1",
    #         ),
    #         href="/start_game",
    #     )


    # def generate_team_button(team_shortName):

    # return dbc.Button(children=str(team_shortName),
    #                   color="primary",
    #                   className="mr-1",
    #                   id=str(team_shortName))

    return df[['hov_txt']].to_dict('records')

