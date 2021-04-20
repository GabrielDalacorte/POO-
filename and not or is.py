'''
Operadores Unários = NOT
Operadores Binários = AND, OR, IS
'''
## AND
# AMBOS VALORES PRECISAM SER TRUE

'''
ativo = True
logado = True
#logado = False =  mostra o else

if ativo and logado:
    print("Bem-Vindo")
else:
    print("Você precisa ativar sua conta no sistema..")
'''

# OR
# UM OU OUTRO VALOR PRECISA SER TRUE

'''
ativo = False
logado = True
#Os dois no false mostrar o ELSE

if ativo or  logado:
    print("Bem-Vindo")
else:
    print("Você precisa ativar sua conta no sistema..")
'''

# NOT
# O VALOR BOLEANO É INVERTIDO, OU SEJA, SE FOR TRUE VIRA FALSE, SE FOR FALSE VIRA TRUE

ativo = True
logado = True
#Se o ativo for True =  Ben-vindo, se não mostra a mensagem de erro

if not ativo:
    print("Você precisa ativar sua conta no sistema..")
else:
    print("Bem-Vindo")

