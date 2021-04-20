"""
List Comprehension

- Utilizando List Comprehension nos podemos gerar novas listas com dados processados a partir de outr
iterável

#Sintaxe de List Comprehension

[ dado for dado in iterável ]

"""

# Exemplos

numeros = [1,2,3]

res = [numero * 10 for numero in numeros]
print(res)

"""
Para entender melhor o que está acontecendo, devemos dividir a expressao em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
"""

    