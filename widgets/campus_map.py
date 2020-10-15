import plotly.graph_objs as go
import dash_html_components as html

MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoianVlc3BhZm84NyIsImEiOiJja2QwcWNiZ28wMTY0MnhwYmNqbDMxaGl0In0.SRdwqTCLquu35-2noY2tEQ'

def get_data(db):

    df = db.get_join_games_df()

    fig = render_map(df)
    table = render_table(df)

    return fig, table


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
        hovertext=df['hov_txt']
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
                    lat=48.71,
                    lon=2.17
                ),
                zoom=11,
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

