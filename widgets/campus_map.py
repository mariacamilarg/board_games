import plotly.graph_objs as go
import dash_html_components as html
import dash_bootstrap_components as dbc

MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoianVlc3BhZm84NyIsImEiOiJja2QwcWNiZ28wMTY0MnhwYmNqbDMxaGl0In0.SRdwqTCLquu35-2noY2tEQ'

def get_data(db, in_next_hours):

    df = db.get_join_games_df()

    # filter df
    df = df[ df["next_hours"] <= in_next_hours ]
    print(df)

    # render
    map_fig = render_map(df)
    games_list = render_list(df)

    return map_fig, games_list


def get_data_game(db, game_id):
    
    df = db.get_join_games_df()

    # filter df
    df = df[ df["id"] == game_id ]
    print(df)

    for i, game in df.iterrows():
        game_id = game["id"]

        img = game["img"]
        name = game["name"]
        when = f'{game["when"]} @ {game["time"]}'
        details = [
            html.I(className='fa fa-clock-o fa-sm'),
            f' {game["duration_str"]} . .',
            html.I(className='fa fa-users fa-sm'),
            f' {game["current_players"]}/{game["max_players"]} . .',
            html.I(className='fa fa-signal fa-sm'),
            f' {game["difficulty"]}/5'
        ]
        category = f'Categories: {game["category"]}'
        href = f"/request_join?id={game_id}"

        return (img, name, when, details, category, href)


def get_data_request(db, game_id, n_interval):
    
    df = db.get_join_games_df()

    # filter df
    df = df[ df["id"] == game_id ]
    print(df)

    open1 = True if n_interval >= 2 else False

    for i, game in df.iterrows():
        game_id = game["id"]

        href_back = f"/join_game?id={game_id}"
        request_info = f'You are requesting to join {game["name"]} for {game["when"]} @ {game["time"]}'

        return (href_back, request_info, open1) 


def render_map(df):

    df["hov_text"] = df['name'] + "<br>Category: " + df['category'] + "<br>Difficulty: " + df['difficulty'].astype(str) + "/5<br># Players: " + df['max_players'].astype(str)

    # Create figure
    locations = [go.Scattermapbox(
        lon=df['longitude'],
        lat=df['latitude'],
        mode='markers',
        marker={'color': df['color'], 'size': 5 * df['factor']},
        unselected={'marker': {'opacity': 1}},
        selected={'marker': {'opacity': 0.5, 'size': 100}},
        hoverinfo='text',
        hovertext=df['hov_text']
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


def render_list(df):

    games_list = []

    for i, game in df.iterrows():
        game_id = game["id"]
        a = html.A(dbc.Row(
            children=[
                dbc.Col(
                    dbc.CardImg(src=game["img"], id=f"img{game_id}"), 
                    width=3
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

    return games_list


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

