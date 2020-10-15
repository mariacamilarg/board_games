import base64
import io
import urllib

import pandas as pd
import plotly.graph_objs as go


def get_number_players():
    df = pd.read_csv("./assets/csv/board_games.csv")
    return df.NUMBER_PLAYERS


def get_name():
    df = pd.read_csv("./assets/csv/board_games.csv")
    return df.NAME
