"""
POO - O metodo super()

O metodo super() se refere a super classe.
"""

class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O animal {self.__nome} fala {som}')

class Cachorro(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca
         

braum = Cachorro('Braum', 'Canino', 'shi-tzu')
braum.faz_som('vai a meda')