# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 14:55:35 2022

Este codigo, visa abordar alguns pontos da prog, em Python para o Metatrader5.

doc:
    https://www.mql5.com/en/docs/integration/python_metatrader5

@author: bpriantti
"""

#import biblios:
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
import pytz

#set display pandas:
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display

# establish connection to MetaTrader 5 terminal:
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")

utc_from = datetime(2020, 1, 10, tzinfo=timezone)
utc_to = datetime(2022, 12, 31, hour = 13, tzinfo=timezone)

#copy rates dataset:
rates = mt5.copy_rates_range("PETR4", mt5.TIMEFRAME_D1, utc_from, utc_to)
 
#finaliza conexao mt5:
mt5.shutdown()

#criando dataframe:
rates_frame = pd.DataFrame(rates)

#convertendo o time:
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
 
# display data
print("\nDisplay dataframe with data")
print(rates_frame.head(10))

#visualizando graficamente de forma simples:
rates_frame.close.plot()