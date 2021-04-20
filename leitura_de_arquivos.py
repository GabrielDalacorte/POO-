"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada,
que neste caso é o nome do arquivo a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.
"""

# Exemplo

arquivo = open('texto.txt')
#print(arquivo)
#print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

print(arquivo.read())