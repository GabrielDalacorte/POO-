"""
StringIO

ATENÇÃO: Para ler ou escrever da

"""

# Primeiro fazemos o import
from io import StringIO

mensagem = 'Este é apenas uma string normal'

arquivo = StringIO(mensagem)
print(arquivo.read())