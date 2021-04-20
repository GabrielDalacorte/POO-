"""
Generators

EM aulas anteriores nos estudamos:
    - List Comprehension
    - DIct Comprehension
    - Set Comprehension

Não vimos:
    - Tuple Comprehension, pois eles se chamam Generators


Generator ocupa menos recurso em memória


nomes = ['Gabriel', 'Gorila', 'Braum']
res = (nome[0] == 'G' for nome in nomes)
print(res)
print(type(res))

# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento 
# passado como parametro.
from sys import getsizeof

print(getsizeof('Geek'))
print(getsizeof('eureheurehreurhueeuheurhe'))

"""


# EU posso iterar no Generator? Sim

gen = (x * 10 for x in range(1000))
print(gen)

for num in gen:
    print(num)