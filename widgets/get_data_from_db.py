import base64
import io
import urllib

import pandas as pd
import plotly.graph_objs as go


def get_price():
    df = pd.read_csv("./assets/csv/buy_sell.csv")
    return df.PRICE


def get_name():
    df = pd.read_csv("./assets/csv/buy_sell.csv")
    return df.NAME

def get_description():
    df = pd.read_csv("./assets/csv/buy_sell.csv")
    return df.DESCRIPTION


def get_img():
    df = pd.read_csv("./assets/csv/buy_sell.csv")
    return df.IMG


def count_lines():
    df = pd.read_csv("./assets/csv/buy_sell.csv")

    return len(df.index)


def rent_get_price():
    df = pd.read_csv("./assets/csv/rent_rent_out.csv")
    return df.PRICE


def rent_get_name():
    df = pd.read_csv("./assets/csv/rent_rent_out.csv")
    return df.NAME

def rent_get_description():
    df = pd.read_csv("./assets/csv/rent_rent_out.csv")
    return df.DESCRIPTION


def rent_get_img():
    df = pd.read_csv("./assets/csv/rent_rent_out.csv")
    return df.IMG


def rent_count_lines():
    df = pd.read_csv("./assets/csv/rent_rent_out.csv")

    return len(df.index)
