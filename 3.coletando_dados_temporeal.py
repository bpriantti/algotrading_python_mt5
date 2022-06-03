# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 14:55:35 2022

Este codigo, visa abordar alguns pontos da prog, em Python para o Metatrader5.

doc:    
    https://www.mql5.com/en/docs/integration/python_metatrader5

@author: bpriantti
"""

#import biblios essenciais:
import pandas as pd
import time

#import biblio mt5:
import MetaTrader5 as mt5

#iniciando o mt5:
mt5.initialize()

#ativo:
ativo = 'PETR4'

while(True):
    time.sleep(2)
    print(mt5.symbol_info_tick(ativo).last)

