"""
Zip

Zip() -> Cria um iteravel (Zip Object) que agrega elementos de cada um dos iteraveis passados
como entrada em pares.



# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))


zip1 = zip(lista1, lista2)
print(list(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

lista3 = [7, 8, 9, 10, 11]


# OBS: O zip() utiliza como parametro o menor tamanho em iterável. Isso signifca que se estiver 
# trabalhando com iteraveis de tamanhos diferentes, irá parar quando os elementos de menor
# iteravel acabar.

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))



# Lista de tuplas

dados = [(0, 1), (1, 2), (4, 5)]

print(list(zip(*dados)))
"""


prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final2))