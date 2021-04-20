"""
POO - Heranca Multipla

Heranca Multipla -> Nada mais e do que a possibilidade de uma classe herdar de multiplas classes
fazendo com que a classe filha herde todos os atributos e metodos de todas as classes herdads.
"""

# Exemplo 1 - Multiderivacao Direta:

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class Multiderivada(Base1, Base2, Base3):
    pass

# Exemplo 2 - Multiderivacao Indireta

class base1:
    pass

class base2(Base1):
    pass

class Base3(base2): #Base3 herdada base 2 e junto a base1 pois a base2 ja tem a base1 herdada
    pass

class Multiderivada(Base3):
    pass