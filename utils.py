'''
Useful functions for checking a tresults, and performs some calculations
'''

import pandas as pd
import numpy as np
import matplotlib as plt
from datetime import datetime
import plotly.graph_objects as go
import yfinance as yf
import investpy


def plot_OHLC(df):

    fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

    fig.show()


def OHLC_to_HA(df):
    df_ha = df.copy()
    for i in range(df_ha.shape[0]):
        if i > 0:
            df_ha.loc[df_ha.index[i],'Open'] = (df['Open'][i-1] + df['Close'][i-1])/2
    
        df_ha.loc[df_ha.index[i],'Close'] = (df['Open'][i] + df['Close'][i] + df['Low'][i] +  df['High'][i])/4
    df_ha = df_ha.iloc[1:,:]
    return df_ha


#need to check at his failure
def get_stock_hist_data(tycker, timeframe_ = '1w', period_ = '2y',
                        country_ = 'United States', start_date = '01/01/2019', 
                        end_date = '01/01/2022'): 
    try:
        df = yf.download(tickers=tycker, period=period_, interval=timeframe_)
    
    except:
        df = investpy.get_stock_historical_data(stock=tycker,
                                                country=country_,
                                                from_date=start_date,
                                                to_date=end_date)
    return df






