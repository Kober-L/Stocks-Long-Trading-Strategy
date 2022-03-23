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
    '''

    #extract the prices
    #select the points
    #then extract them
    #check at if there is a growth of 5.7 between each point (5.7 w.r.t what??)
