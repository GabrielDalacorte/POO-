"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha

# writer() - > Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o metodo
# writenow() para escrever cada linha. Este metodo recebe uma lista.

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritos_csv = writer(arquivo)
    filme = None
    escritos_csv.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme != 'sair':
        filme = input("Informe o nome do filme: ")
        if filme != 'sair':
            genero = input("Informe o genero: ")
            duracao = input("Informe a duracao em minutos: ")
            escritos_csv.writerow([filme, genero, duracao])
"""

# DictWriter

from csv import DictWriter

# OBS: As chaves do dicionario devem ser as mesmas utilizadas como cabecalho.

with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input("Informe o nome do filme: ")
        if filme != 'sair':
            genero = input("Informe o genero: ")
            duracao = input("Informe a duracao em minutos: ")
            escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duracao": duracao})



