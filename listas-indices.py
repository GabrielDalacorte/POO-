'''
#Mostrar o indice
cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

#Para trazer o numero do indice antes

cores = ['verde', 'amarelo', 'azul', 'branco']
for indice, cor in enumerate(cores):
    #print(indice,cor)
    print(indice,' = ', cor)

#Outros metodos não tão importantes mas tambem uteis
#ENCONTRAR O INDICE DE UM ELEMENTO NA LISTA

numeros = [1, 2, 3, 5, 77 ,989, 443, 34342, 333, 445]

#Em qual indice esta o numero 77
print(numeros.index(77))

#Em qual indice esta o numero 333
print(numeros.index(333))

#Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(443, 1) #Buscando a partir do índice 1
numeros = [1, 2, 3, 5, 77 ,989, 443, 34342, 333, 445]

#Podemos fazer busca dentro de um range inicio/fim
print(numeros.index(77, 2, 6))
#Buscar o indice do valor 989 entre os indices 1 e 7

#Trabalhando com slice de lista com o parametro 'inicio'

#lista[inicio:fim:passo]
lista = [1, 2, 3, 4]
print(lista[1:]) #Iniciando no indice e pegando todos os elementos restantes

#Trabalhando com slice de lista com o parametro 'fim'
print(lista[:2]) #Começa em 0 e pega ate o indice 2 -1

#Trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2]) #começando do 1 e vai ate o final pegando os valores de 2 em 2


#Copiando uma lista para outra (Shallow Copy e Deep Copy)

#  DEEP COPY
lista = [1, 2, 3, 4, 5, 6]
nova = lista.copy()
print(nova)
nova.append(7)
print(nova)
print(lista)
#Veja que ao utilizarmos lista.copy copiamos os dados da lista para uma nova lista, mas elas
#ficaram totalmente independentes ou seja modificando uma lista nao afeta outra. Isso em python
#se chama Deep Copy(Copia profunda)

# SHLlLOW COPY
lista = [1, 2, 3, 4, 5, 6]
nova = lista
print(nova)
nova.append(7)
print(nova)
print(lista)

# Veja que utilizamos a copia via atribuicao e copiamos os dados da lista para a nova lista,mas
# apos realizar modificacoes em uma das listas essa modificacao se refletiu em ambas as listas e isso
# em python e chamado de Shallow Copy
'''