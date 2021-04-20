"""
Metodos de Data e hora

import datetime

# Com now() podemos especificar um timezone (Fuso Horario)
agora = datetime.datetime.now() # now() == agora
print(agora)

hoje = datetime.datetime.today() # today == hoje
print(hoje)
print(type(hoje))

===================
import datetime
# Mudancas ocorrendo a meia-noite - combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
# Ele adicionou um dia e boto meia noite - como se tivesse dizendo que a meia noite do proximo dia ele faria a manutencao.
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

import datetime

# Encontrar o dia da semana, weekday()

# Os dias da semana do metodo weekday() comecam em 0, sendo esta a segunda-feira

# 0 - Segunda feita (monday)
# 1 - Terca feira (tuesday)
# 2 - Quarta feira (wednesday)
# 3 - Quinta feira (thursday)
# 4 - Sexta feita (friday)
# 5 - sabado (saturday)
# 6 - domingo (sunday)
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday()) # ele trouxe 3 (quinta) porque ele botou hoje + 1 dia = quarta + 1 = quinta

import datetime


# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime('%d/%m/%Y') #se por o Y em minusculo, ao inves de trazer 2021 ele traz 21
#hoje_formatado = hoje.strftime('%d/%b/%Y') # 17/Feb/2021
#hoje_formatado = hoje.strftime('%d/%B/%Y') # 17/February/2021
print(hoje_formatado)

 
"""
import datetime
from textblob import TextBlob, translate
import textblob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()

print(formata_data(hoje))
