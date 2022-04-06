import pandas as pd
import numpy as np
import tulipy as ti


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
    #tasso di crescita rispetto al punto precedente
    for i in range(len(points) - 1):
        start_price = points[i]
        next_price = points[i + 1]
        one_perc = start_price / 100
        delta = next_price - start_price
        perc_change = delta / one_perc
        if not (perc_change >= growth):
            return False
        
    return True


#indicators (STILL HAVE TO TEST THEM!)
def calculate_ema(prices, days):
    column = prices['Adj Close']
    column = np.array(column)
    return ti.ema(column, days)


def calculate_ma(prices, days):
    column = prices['Adj Close']
    column = np.array(column)   
    return ti.sma(column, days)
    #return prices.rolling(days, min_periods=1).mean()


def compute_slope(x1, y1, x2, y2):
  return (y2 - y1) / (x2 - x1)


#def up_trend(y1, y2, target_up_trend):
#  return (y2 - y1) >= target_up_trend

