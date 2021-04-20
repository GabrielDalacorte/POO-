"""

Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - Sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir
a -> Abre para escrita, adicionando o conteúdio ao final do arquivo.
+ -> Abre para o modo de atualização: leitura e escrita.

#OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo
conteúdo será adicionado ao final.

# Exemplos X

try:
    with open('testandosetem.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo')
except FileExistsError:
    print("Arquivo já existe.")

# Exemplos A

with open('novo.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

"""

with open('texto.txt', 'r+') as arquivo:
    #arquivo.seek(0)
    arquivo.write("Noqsqsqqsqs topo!\n")
    arquivo.write("Mais uma linha.\n")
     

