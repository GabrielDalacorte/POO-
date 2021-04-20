"""

OBS: Em algumas linguagens de programação os dicionarios python são conhecidos
por mapas.

Dicionarios sao colecoes do tipo chave/valor


# Forma1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))


# Acessando Elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises['br'])
print(paises['py'])

#Forma 2 - Acessando via Get (RECOMENDADA)

print(paises.get('br'))
print(paises.get('eua'))

===============================

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('eua')

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Não encontrei o pais')


#O valor que esta depois do "eua" na variavel pais, so ia aparecer quando a primeira chamada for False
#Em: se no lugar de eua fosse "ru" ia mostrar "Não encontrado"
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('eua', 'Nao encontrado')

print(f'Encontrei o pais {pais}')



localidades = {
    (32.000, 32.99999): 'Escritório em New York',
    (42.000, 98.00909): 'Escritório na Alemanha',
    (32.444, 22,42422): 'Escritório em Porto Alegre'
}

print(localidades)
print(type(localidades))


#Adicionar elementos no dicionarios
receita = {
    'Janeiro': 1840.45,
    'Fevereiro': 1240.45,
    'Março': 2100.45
}
print(receita)

#Forma 1 de adicionar ao dicionario - MAIS COMUM
receita['Maio'] = 2300.00
print(receita)

#Forma 2 de adicionar ao dicionario - MENOS COMUM
novo_dado = {'Junho': 3200.00}
receita.update(novo_dado)
print(receita)

#Atualizando dados em um dicionario
#Forma 1
receita['Maio'] = 550
print(receita)

#Forma 2
receita.update({'Junho': 4500.23})
print(receita)

#CONCLUSÃO1 : A forma de adicionar elementos ou atualizar dados em um dicionarios é a mesma.
#CONCLUSÃO2 : Em dicionarios NÃO podemos ter chaves repetidas

#Como remover dados de um dicionario
receita = {
    'Janeiro': 1840.45,
    'Fevereiro': 1240.45,
    'Março': 2100.45
}

print(receita)
#Forma 1 ---- MAIS COMUM
ret = receita.pop('Março') #retorna valor 300. Se tirar a variavle antes ele não retorna
print(ret)
print(receita)
#OBS1: Aqui precisamos SEMPRE informar a chave, caso não encontre o elemento um KEYERROR é retornado
#OBS2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

#Forma2
del receita['Fevereiro']
print(receita)
#OBS1: Neste caso o valor removido não é retornado
#OBS2: Se a chave não existir sera gerado um KEYERROR


#Imagine que você tem um comércio eletronico, onde temos um carrinho de comprar na qual adicionamos produtos.

Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;

# 1 - Poderiamos utilizar uma Lista para isso? Sim
carrinho = []
produto1 = ['Playstatio4', 1, 2300.00]
produto2 = ['God of War 4',1, 250.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
#OBS: Teriamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos utilizar uma Tupla para isso? Sim
produto1 = ('Playstatio4', 1, 2300.00)
produto2 = ('God of War 4',1, 250.00)
carrinho = (produto1, produto2)
print(carrinho)
#OBS: Teriamos que saber qual é o indice de cada informação do produto.

# 3 - Poderiamos utilizar um dicionario para isso? Sim
carrinho = []
produto1 = {'nome': 'Playstation4', 'quantidade': 1, 'preço': 2300}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 200}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
#OBS: Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
#podemos ter a certeza sobre cada informação


# Métodos dicionario
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionarios = Zerar dados
d.clear()
print(d)

# Copiando um dicionarios para outro
# Forma 1 - DEEP COPY
novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 -  SHALOW COPY
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)

"""
