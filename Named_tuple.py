"""
Module Collections - Named Tuple

Named Tuple -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
"""
# Importando
from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade','raca','nome'])

# Usando
braum = cachorro(idade=2, raca='Shitzu', nome='Braum')
print(braum)

# Acessando os dados
# Forma 1
print(braum[0]) #Idade
print(braum[1]) #Raça
print(braum[2]) #Nome

# FOrma 2 - Mais usada & melhor
print(braum.idade) # Idade
print(braum.raca) # Raça
print(braum.nome) # Nome
print(braum.index('Shitzu')) # Index
print(braum.count('Shitzu')) # Vezes que aparece