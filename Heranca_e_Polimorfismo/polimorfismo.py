"""
POO - Polimorfismo

Pli -> Muitas
Morfis -> Formas


Quando a gente reimplementa um metodo presente na classe pai, nas classes filhas, estamos
realizando um sobrescrita de metodo, chamada (Overriding).

O Overrring e a melhor representacao do Polimorfismo
"""

class Animal(object):
    def __init__(self, nome):
        self.__nome = nome
    
    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar este metodo.")
        # Esta lancando uma exessao.

    def comer(self):
        print(f'{self.__nome} esta comendo....')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala waua waua')

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau miau')

class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} falar snif snif')

# Testes

braum = Cachorro("Braum")
braum.falar()
braum.comer()

gat = Gato("Gatin")
gat.falar()
gat.comer()

mickey = Rato("Mickey")
mickey.falar()
mickey.comer()
