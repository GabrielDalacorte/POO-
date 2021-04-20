"""
Reverse

OBS: Não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona em lista.

Já a função reversed() funciona com qualquer iterável

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator
"""

lista = [1, 2, 3, 4, 5]
res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto

# Lista
print(list(reversed(lista)))
# Tupla
print(tuple(reversed(lista)))
# Conjunto - (Set)
print(set(reversed(lista))) # Em conjunto não definimos a ordem dos elementos

# Podemos iterar sobre o reversed

for letra in reversed("Geek University"):
    print(letra, end='')

# Podemos fazer o mesmo sem o uso do for
print('\n')
print("".join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais facil com o Slice de strings

print("geek university"[::-1])
