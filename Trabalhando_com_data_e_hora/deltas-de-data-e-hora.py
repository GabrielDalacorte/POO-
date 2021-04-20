"""
Trabalhando com deltas de data e hora

delta = diferenca

data_inicial = dd/mm/yyyy 12:55:33.203232
data_final = dd/mm/yyyy 13:34:23.320329

delta = data_final - data_inicial


import datetime

# data que temos hoje
data_hoje = datetime.datetime.now()

# data do aniversario
aniversario = datetime.datetime(2021, 5, 28, 0)

# calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(tempo_para_evento)
# // 60 // 60 divide tudo e dps divide o resto
print(f' Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas...')
"""

import datetime

data_da_compra = datetime.datetime.now()
print(data_da_compra)

regra_do_boleto = datetime.timedelta(days=3)
print(regra_do_boleto)

vencimento_boleto = data_da_compra + regra_do_boleto
print(vencimento_boleto)