import pandas as pd
import os

class Database():

    def __init__(self):
        self.all_board_games = pd.read_csv("./assets/csv/bgg_db_2018.csv")

    def get_all_board_games(self):
        filtered_columns = ["game_id","names","min_players","max_players","avg_time","avg_rating","image_url","age","mechanic","category","weight"]
        return self.all_board_games[filtered_columns]

    def get_join_games_df(self):

        df = pd.DataFrame(data={
            'id': [1, 2],
            'latitude': [48.7066848, 48.7027157], 
            'longitude': [2.166689, 2.1776856], 
            'color': ['#1f9539', '#1f9539'],
            'factor': [5, 5],
            'hov_txt': ['SETTLERS OF CATAN', 'UNO'],
        })

        return df
