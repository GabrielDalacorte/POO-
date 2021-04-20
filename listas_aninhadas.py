"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java/Php) possuem uma estrutura de dados 
chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimencionais (Matrizes);

Em Python nos temos as Listas

numeros = [1, 'b', 3.234, True, 5]

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3
print(listas)
print(type(listas ))

# Como fazemos para acessar os dados?

print(listas[0][1]) #Linha 0 - coluna 1 = 2
print(listas[1][1]) #Linha 1 - coluna 1 = 5


# Iterando com loops em uma lista aninhada
for lista in listas:
    for numero in lista:
        print(numero)

# List Comprehension

print("List Comprehension") 
[[print(valor) for valor in lista] for lista in listas]

"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

# Outros exemplos

# Gerando um tabuleiro/matrix 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)