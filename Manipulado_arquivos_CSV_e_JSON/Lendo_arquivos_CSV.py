"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Virgula

# Separador por Virgula
    1, 2, 3, 4
    'geek', 'nunes', 'python'

# Separador por Ponto e Virgula
    1; 2; 3; 4
    'geek'; 'nunes'; 'python'

# Separador por Espaco
    1 2 3 4
    'geek' 'nunes' 'python'

http://dados.gov.br/dataset

# Possivel de se trabalhar mas nao e o ideal (Trabalhoso)
with open('lutadores.csv', encoding="utf8") as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    #print(type(dados))
    print(dados)

======================================

# Reader
from csv import reader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pular o cabecalho
    for linha in leitor_csv:
        # Cada linha e uma lista
        print(f'{linha[0]} naceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros')
    

# DictReader - Segunda forma

from csv import DictReader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha e um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")    
"""

# DictReader - Com outro separador (nao virgula)

from csv import DictReader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',') #Colocar o separador entre aspas
    for linha in leitor_csv:
        # Cada linha e um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")