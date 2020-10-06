import pandas as pd
import os

class Database():

    def __init__(self):
        self.all_board_games = pd.read_csv("./assets/csv/board_games.csv")

    def get_all_board_games(self):
        return self.all_board_games