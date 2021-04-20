"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja
funções anônimas.

# Função em Python

def funcao(x):
    return 3 * x + 1

print("Val def: ",funcao(6))

====================================================

        UTILIZANDO LAMBA
        UTILIZANDO LAMBA
        UTILIZANDO LAMBA
        UTILIZANDO LAMBA
        UTILIZANDO LAMBA

====================================================
# Expressão Lambda

lambda x: 3 * x + 1

# Como utilizar a expressão Lambda
calc = lambda x: 3 * x + 1
print("Val lamda: ",calc(5))

# Podemos ter expressões Lambdas com multiplas entradas.

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' GaBRIEL   ','nunes '))

# Em função python podemos ter nenhuma ou várias entradas. Em lambdas tambem.

amar = lambda: "Como não amar python? "

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5


print(amar)
print(uma(2))
print(duas(5, 7))

    # se passarmos mais argumentos que parametros esperados teremos TypeError



# Outros Exemplos ( Refazer este de outras formas porque nao entendi muito )

autores = ['Isaac Asimov', 'Ray Bradburry', 'Douglas Admas']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
"""

# Função Quadratica

#f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função F(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))