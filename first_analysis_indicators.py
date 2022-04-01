import pandas as pd
import numpy as np


def detect_trend(prices, points = 8, candles = 104, growth = 5.1, long = True):
    '''
    Input:
        -prices: pandas dataframe with prices derived from a 50MA --> a series that is adj close price 
        -points: the number of prices I want to check in orer to see if there is enough growth
        -candles: the evaluation time of the trend: 104 candles = 2 years
        -growth: the percentage of growth between two points
        -long: determine if we want to detect a long or short trend

    This functions check at prices, taking n points that are prices and veryfies if there is enough growth between them
    '''

    #be sure you are considering only the interested period (the correct amount of candles)
    prices = prices.tail(candles)
    i = 0
    points = []
    for index, row in prices.items():
        if i % 13 == 0:
            points.append(row)
        else:
            pass

        i += 1
    
    #now that you extracted to consider prices, check th proper growth
    #tasso di crescita rispetto al punto precedente o in generale??
    for i in range(len(points) - 1):
        start_price = points[i]
        next_price = points[i + 1]
        one_perc = start_price / 100
        delta = next_price - start_price
        perc_change = delta / one_perc
        if not (perc_change >= growth):
            return False
        
    return True







        

#dopo metti MA(questi devono ritornare solo la colonna adj close!), EMA, slope indicators

    #extract the prices
    #select the points
    #then extract them
    #check at if there is a growth of 5.7 between each point (5.7 w.r.t what??)
