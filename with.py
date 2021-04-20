"""
Passo para trabalhar com um arquivo:

1 - Abrir o arquivo:
arquivo = open("texto.txt")

2 - Trabalhar o arquivo:
print(arquivo.read())

3 - Fechar o arquivo:   
arquivo.close()

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados apos o bloco with

"""

# O block with - Forma Pythonica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
 