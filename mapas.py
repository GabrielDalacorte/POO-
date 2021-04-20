"""
Mapas -> Conhecidos como dicionarios em python

# Iterar sobre dicionarios
for chave in receita:
    print(receita)

for chave in receita:
    print(receita[chave])

for indice, chave in enumerate(receita):
    print(f'{indice} = {chave}: {receita[chave]}')


    #ACESSANDO AS CHAVES
print(receita.keys())

    # Modo pythonico - Recomendado
for x in receita.keys():
print(receita[x])

    # Acessando os valores
print(receita.values())

for x in receita.values():
    print(x)

receita = {'jan': 850.00, 'fev': 1200, 'março': 1400}
print(receita)

# soma , valor maximo, valor minimo, tamanho

print(sum(receita.values())) # Valor total
print(max(receita.values())) # valor mais alto
print(min(receita.values())) # Valor minimo
print(len(receita)) # Tamanho da lista
"""
receita = {'jan': 850.00, 'fev': 1200, 'março': 1400}
print(receita)

for chave in receita:
    print(receita[chave])

for indice, chave in enumerate(receita):
    print(f'{indice} = {chave}: {receita[chave]}')

for x in receita.keys():
    print(receita[x])
