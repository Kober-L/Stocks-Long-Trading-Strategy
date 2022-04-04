import pandas as pd
import numpy as np
import pandas as pd
import yfinance as yf
import tulipy as ti
import utils
import first_analysis_indicators as FA
import matplotlib.pyplot as plt


#prova del detect trend su dati reali
# df = df = pd.read_csv('data_tests/eur_usd_not_asc.csv')
# df_ha = utils.OHLC_to_HA(df)

# #utils.plot_OHLC(df_ha) #descending
# MA_50 = FA.calculate_ma(df_ha, 50)
# MA_50 = MA_50['Adj Close']

# #utils.plot_series(MA_50)
# print(FA.detect_trend(MA_50)) #return False

#test2 with ascending order
df = df = pd.read_csv('data_tests/GOOG_ascending.csv')
df_ha = utils.OHLC_to_HA(df)

utils.plot_OHLC(df_ha) 
MA_50 = FA.calculate_ma(df_ha, 50)
MA_50 = MA_50['Adj Close']

utils.plot_series(MA_50)
print(FA.detect_trend(MA_50)) 