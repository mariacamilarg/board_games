#######################################################
# Main APP definition.
#
# Dash Bootstrap Components used for main theme and better
# organization.
#######################################################

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output
from dash.dependencies import Input, Output, State

from backend import database
from widgets import context_menu, table, campus_map
from pages import web_app, join_game#, large_screen, visor


# APP DEFINITION

app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],)
application = app.server

# We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([context_menu.layout]),
    html.Div(id='page-content'),
])


# DATABASE
db = database.Database()


# CALLBACKS

## Pages routes and components
@app.callback(
    Output('page-content', 'children'),
    [
        Input('url', 'pathname')
    ])
def display_page(pathname):
    if pathname == '/':
        return web_app.layout
    elif pathname == '/join_game':
        return join_game.layout
    # elif pathname == '/large':
    #     return large_screen.layout
    else:
        return '404'

## Games DB
@app.callback(
    [
        Output('all_games_table', 'columns'),
        Output('all_games_table', 'data'),
    ],
    [
        Input('url', 'pathname'),
        #Input('join_game_button', 'n_clicks')
    ],
    [
        
    ]
)
def update_all_games(n_clicks):
    
    print('Updating data table views\n')

    if n_clicks != '/games_db':
        raise dash.exceptions.PreventUpdate()

    columns, data = table.parse_table(db.get_all_board_games())

    return columns, data

## Join Games Page
@app.callback(
    [
        Output('campus_map', 'figure'),
        Output('join_games_table', 'columns'),
        Output('join_games_table', 'data'),
    ],
    [
        Input('url', 'pathname'),
        #Input('join_game_button', 'n_clicks')
    ],
    [
        
    ]
)
def join_game_data(url):
    
    if url != '/join_game':
        raise dash.exceptions.PreventUpdate()

    map_fig, games_table = campus_map.get_data(db)
    games_table_columns = [{"name": i, "id": i} for i in games_table[0].keys()]

    return map_fig, games_table_columns, games_table




# CSS 
external_css = ["https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

# MAIN
if __name__ == '__main__':
    application.run(port=8080)
