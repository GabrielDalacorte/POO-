"""
Funções de Maior Grandeza - Higher Oder Functions - HOF

# Exemplo - Definindo as funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))


# Nested Functions - Funções Aninhadas

# Em Python podemos tambem ter funções dentro de funções, que são conhecidas por Nested Functions
# ou tambem Inner Functions (Funções Internas)

# Exemplos

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(("E ai ", "Suma daqui ", "Gosto muito de você "))
    return humor() + pessoa

# Testando

print(cumprimento('Angelina'))
print(cumprimento('Felicity'))

# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(("KKKKKKKKKKKK", 'UERHEURHUEHE', 'SKAJSKASJAKS'))
    return rir

# Testando

rindo = faz_me_rir()
print(rindo())

"""

# Inner Functions 

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(("KKKKKKKKKKKK", 'UERHEURHUEHE', 'SKAJSKASJAKS'))
        return f'{risada} {pessoa}'
    return dando_risada

# Testando 

rindo = faz_me_rir_novamente("Thasiane")

print(rindo())
print(rindo())
print(rindo())
