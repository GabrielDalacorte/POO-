""" 
Entendendo Iterators e Iterables

Iterator -> 
    - Um objeto que pode ter iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

Iterable ->
    - Um objeto que irá retornar um terator quando a função iter() for chamada.

nome = 'Geek' # É um iterable mas não iterator
numeros = [1, 2, 3, 4, 5] # É um iterable mas não iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1)) # G 
print(next(it1)) # E
print(next(it1)) # E
print(next(it1)) # K

print(next(it2)) # 1
print(next(it2)) # 2
print(next(it2)) # 3
print(next(it2)) # 4
print(next(it2)) # 5

"""

nome = 'Geek'

for letra in nome:
    print(f'{letra}')
