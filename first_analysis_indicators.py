import pandas as pd
import numpy as np


def detect_trend(prices, points = 8, candles = 104, growth = 5.7, long = True):
    '''
    Input:
        -prices: pandas dataframe with prices derived from a 50MA
        -points: the number of prices I want to check in orer to see if there is enough growth
        -candles: the evaluation time of the trend: 104 candles = 2 years
        -growth: the percentage of growth between two points
        -long: determine if we want to detect a long or short trend

    This functions check at prices, taking n points that are prices and veryfies if there is enough growth between them
    '''

    #be sure you are considering only the interested period (the correct amount of candeles)
    prices = prices.tail(candles)
    i = 0
    points_df = pd.DataFrame()
    for index, row in prices.iterrows():
        if i % 13 == 0:
            
        else:
            pass

        i += 1
#continue from this point
        

#dopo metti MA(questi devono ritornare solo la colonna adj close!), EMA, slope indicators

    #extract the prices
    #select the points
    #then extract them
    #check at if there is a growth of 5.7 between each point (5.7 w.r.t what??)
