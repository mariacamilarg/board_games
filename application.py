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
from flask import request
from dash.dependencies import Input, Output
from dash.dependencies import Input, Output, State
import csv
from backend import database

from widgets import context_menu, get_data_from_db, table, campus_map, parse_url, manage_csv_rows
from pages import web_app, buy_sell_rent, join_game, buy_game, rent_game, contact_renter, contact_exchange, \
    see_exchange_game, contact_seller, sell_game, rent_out_game, exchange_game

# APP DEFINITION

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)
application = app.server

# We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # html.Div([context_menu.layout]),
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
    elif pathname == '/sell_game':
        return sell_game.layout
    elif pathname == '/rent_out_game':
        return rent_out_game.layout
    elif pathname == '/exchange_game':
        return exchange_game.layout
    elif pathname == '/contact_seller':
        return contact_seller.layout
    elif pathname == '/rent_game':
        return rent_game.layout
    elif pathname == '/contact_renter':
        return contact_renter.layout
    elif pathname == '/see_exchange_game':
        return see_exchange_game.layout
    elif pathname == '/contact_exchange':
        return contact_exchange.layout
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
        # Input('join_game_button', 'n_clicks')
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
        # Input('join_game_button', 'n_clicks')
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


## PUT DATA IN BUY
@app.callback(
    [
        Output('name1', 'children'),
        Output('price1', 'children'),
        Output('img1', 'src'),
        Output('name2', 'children'),
        Output('price2', 'children'),
        Output('img2', 'src'),
        Output('name3', 'children'),
        Output('price3', 'children'),
        Output('img3', 'src'),
        Output('name4', 'children'),
        Output('price4', 'children'),
        Output('img4', 'src'),
        Output('name5', 'children'),
        Output('price5', 'children'),
        Output('img5', 'src'),
    ],
    [
        Input('url', 'pathname'),
    ]
)
def add_to_card(url):
    if url != '/buy_sell_rent':
        raise dash.exceptions.PreventUpdate()

    number_of_rows = get_data_from_db.count_lines()
    my_list = []

    i = 0
    while i < number_of_rows:
        my_list.append(get_data_from_db.get_name()[i])
        my_list.append(str(get_data_from_db.get_price()[i]) + " €"),
        my_list.append("/assets/images/" + get_data_from_db.get_img()[i])
        i += 1

    number_of_html_cards = 5
    while number_of_rows < number_of_html_cards:
        my_list.append(" ")
        my_list.append(" ")
        my_list.append(" ")
        number_of_rows += 1

    return my_list


## BUY page
@app.callback(
    [
        Output('name_buy_this', 'children'),
        Output('price_buy_this', 'children'),
        Output('description_buy_this', 'children'),
        Output('img_buy_this', 'src'),
        Output('link_buy', 'href'),
    ],
    [
        Input('url', 'pathname'), Input('url', 'search')
    ],
    [

    ]
)
def display_info(url, search_str):
    if url != '/buy_game':
        raise dash.exceptions.PreventUpdate()
    my_id = parse_url.parse_url_id(search_str)
    print(my_id)

    my_list = []
    my_list.append(get_data_from_db.get_name()[int(my_id) - 1])
    my_list.append(str(get_data_from_db.get_price()[int(my_id) - 1]) + str(" €")),
    my_list.append(get_data_from_db.get_description()[int(my_id) - 1]),
    my_list.append("/assets/images/" + get_data_from_db.get_img()[int(my_id) - 1])
    my_list.append("/contact_seller?id=" + my_id)

    return my_list


## SELLER page
@app.callback(
    [
        Output('link_seller', 'href'),
    ],
    [
        Input('url', 'pathname'), Input('url', 'search')
    ],
)
def display_info(url, search_str):
    if url != '/contact_seller':
        raise dash.exceptions.PreventUpdate()
    my_id = parse_url.parse_url_id(search_str)
    print(my_id)

    my_list = []
    my_list.append("/buy_game?id=" + my_id)

    return my_list


########################################################################
## PUT DATA IN RENT
@app.callback(
    [
        Output('rent_name1', 'children'),
        Output('rent_price1', 'children'),
        Output('rent_img1', 'src'),
        Output('rent_name2', 'children'),
        Output('rent_price2', 'children'),
        Output('rent_img2', 'src'),
        Output('rent_name3', 'children'),
        Output('rent_price3', 'children'),
        Output('rent_img3', 'src'),
        Output('rent_name4', 'children'),
        Output('rent_price4', 'children'),
        Output('rent_img4', 'src'),
        Output('rent_name5', 'children'),
        Output('rent_price5', 'children'),
        Output('rent_img5', 'src'),
    ],
    [
        Input('url', 'pathname'),
    ]
)
def add_to_card(url):
    if url != '/buy_sell_rent':
        raise dash.exceptions.PreventUpdate()

    number_of_rows = get_data_from_db.rent_count_lines()
    my_list = []

    i = 0
    while i < number_of_rows:
        my_list.append(get_data_from_db.rent_get_name()[i])
        my_list.append(str(get_data_from_db.rent_get_price()[i]) + " € " + str(get_data_from_db.rent_get_time()[i])),
        my_list.append("/assets/images/" + get_data_from_db.rent_get_img()[i])
        i += 1

    number_of_html_cards = 5
    while number_of_rows < number_of_html_cards:
        my_list.append(" ")
        my_list.append(" ")
        my_list.append(" ")
        number_of_rows += 1

    return my_list


## RENT page
@app.callback(
    [
        Output('name_rent_this', 'children'),
        Output('price_rent_this', 'children'),
        Output('description_rent_this', 'children'),
        Output('img_rent_this', 'src'),
        Output('link_rent', 'href'),
    ],
    [
        Input('url', 'pathname'), Input('url', 'search')
    ],
    [

    ]
)
def display_info(url, search_str):
    if url != '/rent_game':
        raise dash.exceptions.PreventUpdate()
    my_id = parse_url.parse_url_id(search_str)
    print(my_id)

    my_list = []
    my_list.append(get_data_from_db.rent_get_name()[int(my_id) - 1])
    my_list.append(str(get_data_from_db.rent_get_price()[int(my_id) - 1]) + str(" €")),
    my_list.append(get_data_from_db.rent_get_description()[int(my_id) - 1]),
    my_list.append("/assets/images/" + get_data_from_db.rent_get_img()[int(my_id) - 1])
    my_list.append("/contact_renter?id=" + my_id)

    return my_list


## RENTER page
@app.callback(
    [
        Output('link_renter', 'href'),
    ],
    [
        Input('url', 'pathname'), Input('url', 'search')
    ],
)
def display_info(url, search_str):
    if url != '/contact_renter':
        raise dash.exceptions.PreventUpdate()
    my_id = parse_url.parse_url_id(search_str)
    print(my_id)

    my_list = []
    my_list.append("/rent_game?id=" + my_id)

    return my_list


########################################################################
## PUT DATA IN EXCHANGE
@app.callback(
    [
        Output('exchange_wanted1', 'children'),
        Output('exchange_offered1', 'children'),
        Output('exchange_img1', 'src'),
        Output('exchange_wanted2', 'children'),
        Output('exchange_offered2', 'children'),
        Output('exchange_img2', 'src'),
        Output('exchange_wanted3', 'children'),
        Output('exchange_offered3', 'children'),
        Output('exchange_img3', 'src'),
        Output('exchange_wanted4', 'children'),
        Output('exchange_offered4', 'children'),
        Output('exchange_img4', 'src'),
        Output('exchange_wanted5', 'children'),
        Output('exchange_offered5', 'children'),
        Output('exchange_img5', 'src'),
    ],
    [
        Input('url', 'pathname'),
    ]
)
def add_to_card(url):
    if url != '/buy_sell_rent':
        raise dash.exceptions.PreventUpdate()

    number_of_rows = get_data_from_db.exchange_count_lines()
    my_list = []

    i = 0
    while i < number_of_rows:
        my_list.append("WANTS " + get_data_from_db.exchange_get_wanted()[i])
        my_list.append("OFFERS " + get_data_from_db.exchange_get_offered()[i]),
        my_list.append("/assets/images/" + get_data_from_db.exchange_get_img()[i])
        i += 1

    number_of_html_cards = 5
    while number_of_rows < number_of_html_cards:
        my_list.append(" ")
        my_list.append(" ")
        my_list.append(" ")
        number_of_rows += 1

    return my_list


## SEE EXCHANGE page
@app.callback(
    [
        Output('wanted_exchange_this', 'children'),
        Output('offered_exchange_this', 'children'),
        Output('description_exchange_this', 'children'),
        Output('img_exchange_this', 'src'),
        Output('link_exchange', 'href'),
    ],
    [
        Input('url', 'pathname'), Input('url', 'search')
    ],
    [

    ]
)
def display_info(url, search_str):
    if url != '/see_exchange_game':
        raise dash.exceptions.PreventUpdate()
    print(search_str)
    my_id = parse_url.parse_url_id(search_str)
    print(my_id)

    my_list = []
    my_list.append("WANTS " + get_data_from_db.exchange_get_wanted()[int(my_id) - 1])
    my_list.append("OFFERS " + get_data_from_db.exchange_get_offered()[int(my_id) - 1]),
    my_list.append(get_data_from_db.exchange_get_description()[int(my_id) - 1]),
    my_list.append("/assets/images/" + get_data_from_db.exchange_get_img()[int(my_id) - 1])
    my_list.append("/contact_exchange?id=" + my_id)

    return my_list


## EXCHANGER page
@app.callback(
    [
        Output('link_exchanger', 'href'),
    ],
    [
        Input('url', 'pathname'), Input('url', 'search')
    ],
)
def display_info(url, search_str):
    if url != '/contact_exchange':
        raise dash.exceptions.PreventUpdate()
    print(search_str)
    my_id = parse_url.parse_url_id(search_str)
    print(my_id)

    my_list = []
    my_list.append("/see_exchange_game?id=" + my_id)

    return my_list


# def add_to_csv(url):
#
#     if url != '/buy_sell_rent':
#         raise dash.exceptions.PreventUpdate()
#
#     with open('./assets/csv/buy_sell.csv', 'a') as fd:
#         name= "catannn"
#         price = "25€"
#         img= "catan.jpg"
#         description="desc"
#         new_row = [name, price, img, description]
#         writer = csv.writer(fd)
#         writer.writerow(new_row)
#         print(fd)
#     return new_row

#################
## SELL GAME
@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
    [dash.dependencies.Input('sell_button', 'n_clicks')],
    [dash.dependencies.State('sell_game_name', 'value'),
     dash.dependencies.State('sell_game_price', 'value'),
     dash.dependencies.State('sell_game_img', 'value'),
     ])
def update_output(n_clicks, value_name, value_price, value_img):
    if value_name is not None and value_price is not None and value_img is not None:
        row_contents = [value_name, value_price, "catan.jpg"]
        # Append a list as new line to an old csv file
        manage_csv_rows.append_list_as_row('./assets/csv/buy_sell.csv', row_contents)

        return 'Thank you! We have added the game to the relative section.'

    return " "


#################
## RENT GAME
@app.callback(
    dash.dependencies.Output('rent_container-button-basic', 'children'),
    [dash.dependencies.Input('rent_button', 'n_clicks')],
    [dash.dependencies.State('rent_game_name', 'value'),
     dash.dependencies.State('rent_game_price', 'value'),
     dash.dependencies.State('rent_game_time', 'value'),
     # dash.dependencies.State('rent_game_img', 'value'),
     ])
def update_output(n_clicks, value_name, value_price, value_time):
    if value_name is not None and value_price is not None and value_time is not None:
        row_contents = [value_name, value_price, value_time, "catan.jpg"]
        # Append a list as new line to an old csv file
        manage_csv_rows.append_list_as_row('./assets/csv/rent_rent_out.csv', row_contents)

        return 'Thank you! We have added the game to the relative section.'

    return " "


###########
## EXCHANGE GAME
@app.callback(
    dash.dependencies.Output('exchange_container-button-basic', 'children'),
    [dash.dependencies.Input('exchange_button', 'n_clicks')],
    [dash.dependencies.State('exchange_game_name', 'value'),
     dash.dependencies.State('exchange_game_name2', 'value'),
     # dash.dependencies.State('exchange_game_img', 'value'),
     ])
def update_output_exchange(n_clicks, value_name, value_name2):
    if value_name is not None and value_name2 is not None:
        row_contents = [value_name, value_name2, "catan.jpg"]
        # Append a list as new line to an old csv file
        manage_csv_rows.append_list_as_row('./assets/csv/exchange.csv', row_contents)

        return 'Thank you! We have added the game to the relative section.' \
               ' The input value was "{}, {}" and the button has been clicked {} times'.format(
            value_name, value_name2,
            n_clicks
        )
    return " "


# BUY CONTACT
@app.callback(
    [Output("buy_m1", "is_open"),
     Output("buy_m2", "is_open"),
     Output("buy_m3", "is_open"),
     Output("buy_m4", "is_open"),
     Output("buy_m5", "is_open"),
     Output("buy_m6", "is_open"),
     Output("buy_m7", "is_open"),
     Output('label3', 'children'),
     ],
    [Input("url", "pathname"), dash.dependencies.Input('interval3', 'n_intervals')]
)
def messages(path, n):
    if path != '/contact_seller':
        raise dash.exceptions.PreventUpdate()
    num_of_messages = 7
    my_list = []
    i = 1
    while i <= num_of_messages:
        if i <= n+1:
            my_list.append(True)
        else:
            my_list.append(False)
        i = i + 1

    my_list.append('Intervals Passed: ' + str(n))
    return my_list

# RENT CONTACT
@app.callback(
    [Output("rent_m1", "is_open"),
     Output("rent_m2", "is_open"),
     Output("rent_m3", "is_open"),
     Output("rent_m4", "is_open"),
     Output("rent_m5", "is_open"),
     Output("rent_m6", "is_open"),
     Output("rent_m7", "is_open"),
     Output('label2', 'children'),
     ],
    [Input("url", "pathname"), dash.dependencies.Input('interval2', 'n_intervals')]
)
def messages(path, n):
    if path != '/contact_renter':
        raise dash.exceptions.PreventUpdate()
    num_of_messages = 7
    my_list = []
    i = 1
    while i <= num_of_messages:
        if i <= n+1:
            my_list.append(True)
        else:
            my_list.append(False)
        i = i + 1

    my_list.append('Intervals Passed: ' + str(n))
    return my_list

# EXCHANGE CONTACT
@app.callback(
    [Output("exchange_m1", "is_open"),
     Output("exchange_m2", "is_open"),
     Output("exchange_m3", "is_open"),
     Output("exchange_m4", "is_open"),
     Output("exchange_m5", "is_open"),
     Output("exchange_m6", "is_open"),
     Output("exchange_m7", "is_open"),
     Output('label1', 'children'),
     ],
    [Input("url", "pathname"), dash.dependencies.Input('interval1', 'n_intervals')]
)
def messages(path, n):
    if path != '/contact_exchange':
        raise dash.exceptions.PreventUpdate()
    num_of_messages = 7
    my_list = []
    i = 1
    while i <= num_of_messages:
        if i <= n+1:
            my_list.append(True)
        else:
            my_list.append(False)
        i = i + 1

    my_list.append('Intervals Passed: ' + str(n))
    return my_list


# BUY SELL RENT EXCHANGE
@app.callback(
    [Output("buy", "is_open"),
     Output("rent", "is_open"),
     Output("exchange", "is_open"),
     Output("page_title", "children")],
    [Input("buy-button", "n_clicks"), Input("rent-button", "n_clicks"), Input("exchange-button", "n_clicks")],
    [State("buy", "is_open"), State("rent", "is_open"), State("exchange", "is_open")],
)
def toggle_show(n_buy, n_rent, n_exchange, buy_is_open, rent_is_open, exchange_is_open):
    ctx = dash.callback_context

    if not ctx.triggered:
        return True, False, False, "Buy"
    else:

        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "buy-button" and n_buy:
        return not buy_is_open, False, False, "Buy"
    elif button_id == "rent-button" and n_rent:
        return False, not rent_is_open, False, "Rent"
    elif button_id == "exchange-button" and n_exchange:
        return False, False, not exchange_is_open, "Exchange"
    return False, False, False, "Choose a category"


# CSS
external_css = ["https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

# MAIN
if __name__ == '__main__':
    application.run(port=8080)
