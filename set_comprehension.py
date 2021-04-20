"""
Set Comprehension

 
"""

# Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

# Outros exemplos

numeros = {x ** 2 for x in range(10)}

# Desafio!!! Faça uma alteração na estrutura acima para gerar um dicionário ao invés de set

numeros = {valor: valor ** 2 for valor in range(10)} 
print(numeros)


# Para finalizar

letras = {letra for letra in "Geek Unisersity"}
print(letras)