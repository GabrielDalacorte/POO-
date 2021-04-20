"""
Manipulando Data e Hora.

Python tem um modulo built-in (integrado) para se trabalhar com data e hora
chamado datetime


import datetime

#print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

#datetime.MAXYEAR = 2020
#print(datetime.MAXYEAR)

# Retorna a data e hora corrente

print(datetime.datetime.now()) # 2021-02-17 12:59:21.224416 

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()
print(inicio)

# Alterar o horario para 16 horas, 0 minutos, 0 segund, 0 microsegundo

inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)
print(inicio)
========================

# Criando uma data-hora
import datetime

evento = datetime.datetime(2019, 1, 1, 0)
print(evento)

nascimento = input("Informe sua data de nascimento (dd/mm/yyyy): ")
print(nascimento)

nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0])))
print(nascimento)

"""

import datetime

evento = datetime.datetime.now()

# Acessa individual dos elemento da data e hora

print(evento.year) # ano
print(evento.month) # mes
print(evento.day) # dia
print(evento.hour) # hora
print(evento.minute) # minuto
print(evento.second) # segundo
print(evento.microsecond) # microsegundo