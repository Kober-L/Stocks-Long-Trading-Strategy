'''
Useful functions for checking a tresults, and performs some calculations
'''

import pandas as pd
import numpy as np
import matplotlib as plt
from datetime import datetime
import plotly.graph_objects as go
import yfinance as yf


def plot_df(df):

    fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

    fig.show()


df = yf.download(tickers='AAPL', period='1y', interval='1wk')

plot_df(df)
print('done')