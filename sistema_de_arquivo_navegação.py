"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer
uso do módulo os.


"""
# Fazendo o import
import os

#getcwd() -> Pega o current work directory - diretório de trabalhyo corrente
print(os.getcwd())

os.chdir('..')
print(os.getcwd())
