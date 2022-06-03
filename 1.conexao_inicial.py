# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 14:55:35 2022

Este codigo, visa abordar alguns pontos da prog, em Python para o Metatrader5.

doc:    
    https://www.mql5.com/en/docs/integration/python_metatrader5

@author: bpriantti
"""

#use para instalar o modulo do MT5
#pip install MetaTrader5 

#import biblios essenciais:
import pandas as pd

#import biblio mt5:
import MetaTrader5 as mt5

#iniciando o mt5:
mt5.initialize()

#coletando infos da corretora:
info_account = mt5.account_info()

#transformando em dict:
info_account = info_account._asdict()

#visualizando de forma mais legivel:
for prop in info_account:
    print('{} == {}'.format(prop, info_account[prop]),'\n')
    
df0_infod = pd.DataFrame(list(info_account.items()),columns = ['prop','value'])
print(df0_infod)

#finalizando conexao com o Mt5.
mt5.shutdown()