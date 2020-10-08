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
from widgets import context_menu, get_data_from_db, table  # , campus_map
from pages import web_app, buy_sell_rent, join_game, buy_game, contact_seller  # , large_screen, visor

# APP DEFINITION

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
])
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
    elif pathname == '/buy_sell_rent':
        return buy_sell_rent.layout
    elif pathname == '/buy_game':
        return buy_game.layout
    elif pathname == '/contact_seller':
        return contact_seller.layout
    # elif pathname == '/large':
    #     return large_screen.layout
    else:
        return '404'


## Join Games Page
@app.callback(
    [
        Output('all_games_table', 'columns'),
        Output('all_games_table', 'data'),
    ],
    [
        Input('url', 'pathname'),
        # Input('join_game_button', 'n_clicks')
    ],
    [

    ]
)
def update_all_games(n_clicks):
    print('Updating data table views\n')

    if n_clicks != '/join_game':
        raise dash.exceptions.PreventUpdate()

    columns, data = table.parse_table(db.get_all_board_games())

    return columns, data


# BUY SELL RENT EXCHANGE
@app.callback(
    [Output("buy", "is_open"),
     Output("sell", "is_open"),
     Output("rent", "is_open"),
     Output("exchange", "is_open")],
    [Input("buy-button", "n_clicks"), Input("sell-button", "n_clicks"), Input("rent-button", "n_clicks"),
     Input("exchange-button", "n_clicks")],
    [State("buy", "is_open"), State("sell", "is_open"), State("rent", "is_open"), State("exchange", "is_open")],
)
def toggle_show(n_buy, n_sell, n_rent, n_exchange, buy_is_open, sell_is_open, rent_is_open, exchange_is_open):
    ctx = dash.callback_context

    if not ctx.triggered:
        return True, False, False, False
    else:

        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "buy-button" and n_buy:
        return not buy_is_open, False, False, False
    elif button_id == "sell-button" and n_sell:
        return False, not sell_is_open, False, False
    elif button_id == "rent-button" and n_rent:
        return False, False, not rent_is_open, False
    elif button_id == "exchange-button" and n_exchange:
        return False, False, False, not exchange_is_open,
    return False, False, False, False

# CSS
external_css = ["https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

# MAIN
if __name__ == '__main__':
    application.run(port=8080)
