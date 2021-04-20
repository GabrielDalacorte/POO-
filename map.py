"""
Map 

Com map, fazemos mapeamento de valores para função.

import math

def area(r):
    "Calcula a área de um circulo com raio r."
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 8.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Utilizando map - Mais utilizada
# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável
areas = map(area, raios)
print(type(areas))
print(list(areas))

# Forma 3 - Map com Lambda
print("MAP COM LAMBDA")
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.


# Para fixar - Map

# Temos dados iteráveis:

# dados: a1, a2, ...., an

# Temos uma função:

# Função: f(x)

# Utilizando a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(....), f(an)
"""


cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19)]
print(cidades)


# COnvertendo para fireheint
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))