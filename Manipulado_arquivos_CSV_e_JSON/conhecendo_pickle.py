"""
Conhecendo o Pickle

A funcao do Pickle e realizar o seguinte processo:

Objeto Python -> Binarizacao

Binarizacao - Objeto Python

Este processo e chamado de Serializacao/deserializacao

OBS: O modulo picke nao e seguro contra dados maliuciosos desta forma
nao e recomendado trabalhar com arquivos pickle vindo de outras pessoas que voce
nao conheca ou de fontes desconhecidas
"""

import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'O animal {self.__nome} esta comendo')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} esta miando...')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} esta latindo...')

# Fazer a leitura de dados em arquivos Pickle

felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo) # load() = Carrega o arquivo
    print(f'O gato chama-se {gato.nome}') 
    gato.mia()
    print(f'O tipo do gato e {type(gato)}')

    print(f'O cachorro chamase {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro e {type(cachorro)}')
"""
# Fazendo a escrita em arquivos Pickle
with open('animais.pickle', 'wb') as arquivo: # wb = W(Write) B(Binario)
    pickle.dump((felix, pluto) , arquivo) #dump recebe dois parametros

felix = Gato('Felix')
pluto = Cachorro('Pluto')

"""
