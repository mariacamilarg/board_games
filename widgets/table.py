import base64
import io
import urllib

import pandas as pd
import plotly.graph_objs as go

def parse_table(df):
    columns = [{"name": i, "id": i} for i in df.columns]
    data = df.to_dict('records')

    return columns, data
