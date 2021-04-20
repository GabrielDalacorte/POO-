nome = 'Nunes'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)
'''

#Exemplo for 1(Iterando em uma string)
for letra in nome:
    print(letra)
'''

#Exemplo for 2(Iterando sobre uma lista)
'''
for numero in lista:
    print(numero)
'''
#Exemplo for 3(Iterando sobre um ramge)
'''
for numero in range(1, 10):
    print(numero)
'''
'''
for indice, v in enumerate(nome):
    print(nome[indice])

    #se eu n quiser o indice

for _, letra in enumerate(nome):
    print(letra)
#Enumerate = ((0, 'N'), (1, 'u'), (2, 'n'), (3, 'e'), (4, 's'))

for valor in enumerate(nome):
    #Tras somente as letras print(valor[1])
    #Tras somente os indices print(valor[0]) 
    print(valor) 
'''
'''

qtd = int(input("Quantas vezes o loop deve rodar: "))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')
'''
'''
nomes = "pla"
for letra in nomes:
    print(letra, end='')
'''

#Original  = U+1F60D
#Modificado = U0001F60D

for num in range(1, 11):
    print('\U0001F60D' * num)
