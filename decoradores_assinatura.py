"""
Decoradores com diferentes assinaturas 

# Para resolver utilizamos um padrão de projeto chamado Decorator Pattern


# Relembrando

def grita(funcao):
    def aumentar(nome):
        return funcao(nome).upper() # Para deixar somente o nome em Caixa alta - (nome.upper())
    return aumentar


@grita
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhamento de {acompanhamento}, por favor.'

# Testando 

print(ordenar('Picanha', 'Batata Frita'))
#print(saudacao('Gabriel'))


# Refatoranod com a decorator pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhamento de {acompanhamento}, por favor.'



# |Testando

print(saudacao('Gabriel'))
print(ordenar('Picanha', 'arroz'))
"""

# Decorator com Parametro

def verifica_o_primeiro_arg(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro valor precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_o_primeiro_arg('pizza')
def comida_preferida(*args):
    print(args)

@verifica_o_primeiro_arg(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando

print(soma_dez(10, 32)) #42
print(soma_dez(2, 30)) # Mensagem de erro, pois o primeiro argumento não é 10
print(comida_preferida('pizza', 'Lasanha')) # retorna pizza, lasanha
print(comida_preferida('Strogonoff', 'pizza')) # retorna o erro, pois a 'pizza' precisa ser o
                                               # valor recebido