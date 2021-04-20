"""
Try/Except

Utilizando o bloco try/except para tratar erros que podem ocorrer ao nosos código. Previnindo assim que
o programa pare de funcionar e o usuario receba uma mensagem de erro inesperadas.

A forma geral mais simples é:

try:
    //Execução problematica
except:
    //O que deve ser feito em caso de problemas

# Exemplo 1 - Tratando um erro genérico.

try:
    geek()
except:
    print("Deu algum problema")

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

#Exemplo 2
try:
    len(5)
except:
    print("Deu algum erro")

OBS PARA 1 E 2 = TRATAR ERRO DE FORMA GENÉRICA, NÃO É A MELHOR FORMA DE TRATAMENTO DE ERROS,
O IDEAL É SEMPRE TRATAR DE FORMA ESPECIFICA.

# Exemplo 3 - Tratando um erro especifico

try:
    geek()
except NameError:
    print("Você está utilizando uma função inexistente")


# Exemplo 4 - Tratando um erro especifico

try:
    len(5)
except TypeError:
    print("Você está utilizando uma função inexistente")

# Exemplo 5 - Tratando um erro especifico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')


# Exemplo 6 - Podemos efetuas diversos tratamentos de erro de uma vez.

try:
    #len(5)
    print("Geek"[6])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print("Deu um erro diferente")

"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {"nome": "Geek"}

print(pega_valor(dic, "Geek")) #Se botar o "Nome" no lugar de "Geek" ele não retorna "None"