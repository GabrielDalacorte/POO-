"""
Escrevendo em Arquivos


Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir sera criado,
caso ele já exista, o anterior sera apagado e um novo será criado. 

# Exemplo de escrita - Modo 'w' - write (escrita)

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito facil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
 
"""

with open('novo.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

