lista4 = list(range(11))
lista5 = list('Geek Unisersity')
lista1 = [1, 3, 7, 7, 2, 77, 65, 44, 99, 100]
'''
=-=-=-= COMANDOS ESSENCIAIS =-=-=-=
.APPEND =  PARA ADICIONAR VALORES UNICOS OU SUBLISTAS Á LISTAS
EXEMPLO lista.append(3) ou lista.append[3, 4, 5]

.EXTEND =  PARA ADICIONAR VARIOR ELEMENTOS A ALGUMA LISTA
EXEMPLO lista.extend([3, 5, 7])

.COUNT() =  PODEMOS CONTAR QUANTAS VEZES APARECE O ELEMENTO NA LISTA
EXEMPLO print(lista1.count(7)) #Quantos numeros 7 tem na lista
        print(lista5.count('e')) #Quantas letras E tem na lista

.SORT()  =  #PODemos facilmente ordenar uma lista
            lista1.sort()
            print(lista1)

.REVERSE() = #podemos facilmente inverter uma lista
             lista5.reverse()
             print(lista5)

.COPY() = Para copiar lista
            lista6 = lista1.copy()
            print("Lista original ..........",lista1)
            print("Essa é a lista copiada ..",lista6)

LEN = Podemos saber o tamanho de uma lista
      print(len(lista1))

.POP() =  Para remover o ultimo elemento de uma lista
          print(lista1)
          lista1.pop()
          print(lista1)

        #Podemos tambem remover o elemento pelo indice
            print(lista1)
            lista1.pop(2) << Essse é o indice
            print(lista1)

.CLEAR() = Podemos remover todos os itens de uma lista
           print(lista1)
           lista1.clear()
           print("A lista está vazia",lista1)

#Podemos facilmente repetir elementos em uma lista
    nova = [1, 2, 3]
    nova = nova * 3
    print(nova)

.SPLIT() = #Podemos facilmente converter uma string em uma lista
            OBS:: Por padrao o split separa os elemenos da lista por espaço entre elas

            EXEMPLO 1:
            curso = 'Programação em python: Essencial'
            print(curso)
            curso = curso.split()
            print(curso)

            EXEMPLO 2:
            curso = 'Programação,em,python:,Essencial'
            print(curso)
            curso = curso.split(',')
            print(curso)

.JOIN() = #Convertendo uma lista em uma string
          lista6 = ['Programação', 'em', 'python:' ,'Essencial']
          print(lista6)

          OBS:: Abaixo estamos falando: Pega a lista6,
          colado espaço entre cada elemento e transforma em uma string

          curso = ' '.join(lista6)
          print(curso)
          
.SUM = Somando os valores da lista
       lista = [1, 2, 3, 4, 5, 6]
       print(sum(lista))
          
.MAX = Achando o valor maximo da lista
       lista = [1, 2, 3, 4, 5, 6]
       print(max(lista))
       
          
.min = Achando o valor minimo da lista
       lista = [1, 2, 3, 4, 5, 6]
       print(min(lista))       
=================================================================
=================================================================
#PODemos facilmente checar se determinado valor esta na LISTA

num = 3
if num in lista4:
    print(f'encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}'

if 'G' in lista5:
    print('Encontrei a letra')
else:
    print('Não encontrei a letra')

#PODemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

#Podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(7)) #Quantos numeros 7 tem na lista
print(lista5.count('e')) #Quantas letras E tem na lista


#ADD elementos em lista =  append
#OBS: Com o append, nós so conseguimos adicionar 1 elemento por vez

print(lista1)
lista1.append(32)
print(lista1)

#Lista dentro de outra lista
lista1.append([8, 3, 11]) #COLOCA A LISTA COMO ELEMENTO UNICO(SUBILISTA)
print(lista1)

if [8, 3, 11] in lista1:
    print("Encontrei a lista")
else:
    print('Nao encontrei a lista')

#MESMA COISA QUE O APPEND SO QUE ELE ADICIONA SEM O COLCHETE MUITO BOM PARA SER USADO
lista1.extend([111, 222, 333]) #COLOCA CADA ELEMENTO DA LISTA COMO VALOR ADICIONAL A LISTA
#EXTEND NAO ACEITA VALOR UNICO
print(lista1)

#podemos inserir um novo elemento na lista informando a posição do indice
#Mas não tira o valor do indicie que ja estava
lista1.insert(2 ,'Test')

#Podemos facilmente juntar 2 listas
#listatest = lista5 + lista1
lista1.extend(lista5)
print(lista1)

#podemos facilmente inverter uma lista
lista5.reverse()
lista1.reverse()
print(lista5)
print(lista1)


#Podemos copiar uma lista
lista6 = lista1.copy()
print("Lista original ..........",lista1)
print("Essa é a lista copiada ..",lista6)


#Podemos saber o tamanho de uma lista
print(len(lista1))

#Podemos remover o ultimo elemento de uma lista
    print(lista1)
    lista1.pop()
    print(lista1)
    #Podemos tambem remover o elemento pelo indice
        print(lista1)
        lista1.pop(2) << Essse é o indice
        print(lista1)

#Podemos facilmente repetir elementos em uma lista
    nova = [1, 2, 3]
    nova = nova * 3
    print(nova)


#Podemos facilmente converter uma string em uma lista
OBS:: Por padrao o split separa os elemenos da lista por espaço entre elas

EXEMPLO 1:
    curso = 'Programação em python: Essencial'
    print(curso)
    curso = curso.split()
    print(curso)

EXEMPLO 2:
    curso = 'Programação,em,python:,Essencial'
    print(curso)
    curso = curso.split(',')
    print(curso)


#Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'python:' ,'Essencial']
print(lista6)

#Abaixo estamos falando: Pega a lista6, colado espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)


# Iterando sobre uma lista utilizando for

#EXEMPLO 1:
for elemento in lista5:
    print(elemento)

ou
#EXEMPLO 1: PARA MOSTRAR O RESULTADO FINAL EM BAIXO = GEEK UNIVERSITY
soma = ''
for elemento in lista5:
    print(elemento)
    soma = soma + elemento
print(soma)

#EXEMPLO 2
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#Mostrar o indice

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)
 indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


#Gerar o numero do indice

#Para trazer o numero do indice antes 
cores = ['verde', 'amarelo', 'azul', 'branco']
for indice, cor in enumerate(cores):
    print(indice, cor)
'''


