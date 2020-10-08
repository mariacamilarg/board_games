import base64
import io
import urllib

import pandas as pd
import plotly.graph_objs as go


def parse_table(df):
    columns = [{"name": i, "id": i} for i in df.columns]
    data = df.to_dict('records')

    return columns, data


def get_column(column):
    df = pd.read_csv("./assets/csv/bgg_db_2018.csv")
    print(df[column])
    return df[column]
