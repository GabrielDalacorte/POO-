"""
**Kwargs

Poderiamos chamar este parãmetro de **xis, mas por convenção chamamos de **Kwargs

Este é só mais um parametro, mas diferente do *args que coloca os valores extra em uma tupla,
o **Kwargs exige que utilizemos parametro nomeados e transfomar esses parametro extras em um
dicionario

"""

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos="verde", braum="amarelo", thasi='rojo', gabriel="vermelho")
