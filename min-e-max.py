"""
Min e Max

max() - Retorna o maior vlaor em um iteravél ou o maior de dois ou mais elementos.

# Elementos

lista = [1, 4, 6, 33, 2]
print(max(lista)) # 33

dicionario = {'a': 12, 'b': 32, 'c': 3}
print(max(dicionario)) #b
print(max(dicionario.valyes())) # 32

# Faça um programa que receba dois valores do usuário e mostre o maior

val1 = int(input('Valor: '))
val2 = int(input('Valor: '))

print(max(val1, val2))

min() - retorna o menor valor em um iteravel, pode usar todos os exemplos do max, so que troca por min


# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ohurusbagos']

print(max(nomes)) # Pega a letra com maior valor = Ex: A maior letra do alfabeto
print(min(nomes)) # Pega a letra com menor valor = Ex: A primiera letra do alfabeto

# Pelo TAMANHO DO NOME
print(max(nomes, key=lambda nome: len(nome))) # Ohurusbagos
print(min(nomes, key=lambda nome: len(nome))) # Tim
 
"""


musicas = [
    {"titulo": "Alguma1", "tocou": 3},
    {"titulo": "Alguma2", "tocou": 5},
    {"titulo": "Alguma3", "tocou": 9},
    {"titulo": "Alguma4", "tocou": 13}
]

# DESAFIO - Imprima somente o titulo da musica mais e menos tocada.
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])


# DESARIO - Como encontrar a musica mais tocada e a menos tocada sem usar (max), min(), lambda()
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])
 