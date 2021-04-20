"""
Modulo Collections: Ordened List

OrdenedDict -> É um dicionario, que nos garante a ordem da inserção dos elementos.

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
"""
from collections import OrderedDict
#Entendendo a diferenca entre Dic e Ordened Dict
#Dicionarios comuns

dict1 = {'b':2, 'a':1}
dict2 = {'a':1, 'b':2}
print(dict1 == dict2) #True -> Já que a ordem dos elementos não importa para o dicionario

#Ordened Dict

odict1 = OrderedDict({'b':2, 'a':1})
odict2 = OrderedDict({'a':1, 'b':2})
print(odict1 == odict2)