# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 14:55:35 2022

Este codigo, visa abordar alguns pontos da prog, em Python para o Metatrader5.

doc:
    https://www.mql5.com/en/docs/integration/python_metatrader5

@author: bpriantti
"""

#import biblios:
import pandas as pd
import time
import MetaTrader5 as mt5
from datetime import datetime

#sets:
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1500)


#iniciando o mt5:
mt5.initialize()

#ativo:
ativo = 'PETR4'

#set copy rates ativo:
candles_OHLC = mt5.copy_rates_from(ativo, mt5.TIMEFRAME_D1,datetime.today() ,10)

#transformar para dataframe:
data_candle = pd.DataFrame(candles_OHLC)

print(data_candle.head(10))
print('')

#ajuste do time:
data_candle['time'] = pd.to_datetime(data_candle['time'], unit = 's')

print(data_candle.head(10))

