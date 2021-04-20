'''
#Tupla precisa ter mais de um elemento nela

tupla1 = (4) #ISSO NAO E UMA LISTA
print(type(tupla1))

# Pode fazer isso
tupla2 = (4,) #iSSO E UMA LISTA
#tupla2 = 4,
print(type(tupla2))

#Isso tambem e uma tupla
tupla3 = 1, 2, 3, 4
print(tupla3)
print(type(tupla3))

#Podemos gerar uma tupla dinamicamente com range
#Tupla com range
tupla = tuple(range(11))
print(tupla)

#.SUM = Somando os valores da tupla
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))

#.MAX = Achando ovalor maximo da tupla
tupla = (1, 2, 3, 4, 5, 6)
print(max(tupla))

#.min = Achando o valor minimo da tupla
tupla = (1, 2, 3, 4, 5, 6)
print(min(tupla))
'''
