import pandas as pd
import os

class Database():

    def __init__(self):
        self.all_board_games = pd.read_csv("./assets/csv/board_games.csv")

    def get_all_board_games(self):
        return self.all_board_games

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
