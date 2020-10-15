import base64
import io
import urllib

import pandas as pd
import plotly.graph_objs as go
from urllib.parse import urlsplit, parse_qs
import urllib.parse as urlparse
from urllib.parse import parse_qs
from csv import writer


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='\n') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
