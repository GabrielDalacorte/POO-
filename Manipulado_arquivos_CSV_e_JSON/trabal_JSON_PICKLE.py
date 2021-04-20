"""
JSON - Pickle

JSON -> JavaScript Object Notation

API -> Sao meios de comunicacao entre os servicos oferecidos por empresas (Twitter, Facebook, Youtube..)
e terceiros (Nos desenvolvedores)


import json 

# dumps -> Faaz a formatacao de aspas simples ('') para aspas duplas ("") pois o JSON nao trabalha
# com aspas simples

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])
print(type(ret))
print(ret)

=======================
import json

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self._raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca
    

felix = Gato('Felix', 'Vira-Lata')
print(felix.__dict__)
ret = json.dumps(felix.__dict__)

print(ret)

Integrando o JSON com o Pickle

pip install jsonpickle

import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self._raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')
ret = jsonpickle.encode(felix)
print(ret)
================================

# ESCREVENDO O ARQUIVO JSONPICKLE

import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self._raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
"""
import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self._raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self._raca

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)


