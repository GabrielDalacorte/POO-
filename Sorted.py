"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que ja estudamos em Listas. O sort()
só funciona em listas.


Podemos utilizar o sorted() com qualquer iteravel.

Como o próprio nome ja diz, sorted() serve para ordenar.

OBS: O sorted() sem retorna uma lista, com os elementos do iteravel ordenados


numeros = [6, 4, 7, 22, 0, 3]
print(numeros)
print(sorted(numeros)) #ordenar do menor para o maior

numeros = [6, 4, 7, 22, 0, 3]
#Adicionando parametros ao Sorted()
print(sorted(numeros))
print(sorted(numeros, reverse=True)) #Do maior para o menor



# Podemos utilizar o Sorted() para coisas mais complexas.

usuarios = [
    {"username": "samuel", "tweets":["Eu adoro bolos," "Eu adoro pizaa"]},
    {"username": "jeff", "tweets":[]},
    {"username": "ugauga123", "tweets":["naoanoanoano"]},
    {"username": "gabriel", "tweets":[]},
    {"username": "thasi", "tweets":["Eu adoro pizaa"], "cor": "amarelo", "musica": "rock"},
]


# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"])) # Ordem alfabética.
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True)) # Agora a ordem é reversa.

# Ordenando pelo numero de tweets

print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]))) #Do menor para o maior
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]), reverse=True)) #Do maior para o menor
"""

# Último exemplo

musicas = [
    {"titulo": "Alguma1", "tocou": 3},
    {"titulo": "Alguma2", "tocou": 5},
    {"titulo": "Alguma3", "tocou": 9},
    {"titulo": "Alguma4", "tocou": 13}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))
# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))