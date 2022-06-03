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

#import biblio mt5:
import MetaTrader5 as mt5

#iniciando o mt5:
mt5.initialize()

#verificando ativos:
ativos = mt5.symbols_total()

if ativos > 0:
    print('Total Ativos Disponiveis: ', ativos)
else:
    print('Nenhum Ativo Disponivel')
    
#verificando o nome dos ativos:
ativos = mt5.symbols_get()

#verificando ativos com petr:
petr_sim = mt5.symbols_get('*PETR*')
print(len(petr_sim))

#verificando o nome:
for disp in petr_sim:
    print(disp.name)

print('')

#verificado informacoes sobre o ativo:
ativo = 'PETR4'

sel = mt5.symbol_select(ativo, True)
info_simbolo = mt5.symbol_info(ativo)
info_simbolo_dict = mt5.symbol_info(ativo)._asdict()

print('Informacoes, ', ativo)

for prop in info_simbolo_dict:
    print('{} == {}'.format(prop, info_simbolo_dict[prop]))
    
mt5.shutdown()