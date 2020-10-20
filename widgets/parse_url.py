import base64
import io
import urllib

import pandas as pd
import plotly.graph_objs as go
from urllib.parse import urlsplit, parse_qs
import urllib.parse as urlparse
from urllib.parse import parse_qs


def parse_url_id(str):
    query = urlsplit(str).query
    params = parse_qs(query)
    return params.get('id')[0]
