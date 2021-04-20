"""
Módulo Collections - Counter(Contador)

Collection -> High-performance container Datetypes

Counter -> Recbe um iteravel como parametro e cria um objeto do tipo collection counter que é parecido
com um dicionarios, contendo como chave o elemento da lista, passado como parametro e como valor a
quantidade de ocorrências desse elemento.

# Realizando o import

from collections import Counter

# Exemplo => 1
#Podemos utilizar qualquer iteravel. Aqui usamos uma lista
lista = [1,1,1,1,2,2,24,5,2,2,4,6,6,7,7,2,23,56,12,66,1233,44,33,44]

# Utilizando o counter
res = Counter(lista)
print(res)
print(type(res))

#Counter({2: 5, 1: 4, 6: 2, 7: 2, 44: 2, 24: 1, 5: 1, 4: 1, 23: 1, 56: 1, 12: 1, 66: 1, 1233: 1, 33: 1})

#Veja que para cada elemento da lista, o counter criou uma chave e colocou como valor a quantidade de ocorrencias
#Exemplo 2(numero):5(quantidade de vezes que apareceu na lista)

#Exemplo => 2
print(Counter('Geek University'))
#Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""

# Realizando o import

from collections import Counter

# Exemplo => 3

texto = """
     is simply dummy text of the printing and typesetting industry. 
     Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
     when an unknown printer took a galley of type and scrambled it to make a 
     specimen book. It has survived not only five centuries, but also the leap 
     into electronic typesetting, remaining essentially unchanged. It was popularised 
     in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
     and more recently with desktop publishing software like Aldus PageMaker 
     including versions of Lorem Ipsum.
"""
palavras = texto.split()
#print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))

