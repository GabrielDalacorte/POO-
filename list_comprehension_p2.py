"""

List Comprehension

Nós podemos adicionar estruturas condicionais lógicas ás nossas List Comprehension

"""

# Exemplos

# 1

numeros = [1,2,3,4,5,6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Refatorar

# Qualquer número PAR módulo de 2 é 0 e 0 em python = False. not false = True
pares1 = [numero for numero in numeros if not numero % 2]
impares2 = [numero for numero in numeros if numero % 2]
print(pares1)
print(impares2)