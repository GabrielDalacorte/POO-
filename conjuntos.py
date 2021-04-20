"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a teoria dos conjuntos
da matematica.


Os conjuntos(sets) são referenciados em chaves {}

Diferença entre conjuntos(sets) e mapas(dicionarios) em python:
    - Um dicionario tem chave/valor;
    - Um conjunto tem valor;
    ... Conjuntos não são indexados.

#Definindo conjuntos:

#Forma 1 - Menos comum
s = set({1, 2, 3, 5, 7, 3, 5, 8, 2}) #Repare que temos valores repetidos.
print(s)
print(type(s))

#OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente o mesmo sera ignorado
# sem gerar erros e não fará parte do conjunto.

#Forma 2 - Mais comum
s = ({1, 2, 3, 5, 7, 3, 5, 8, 2})
print(s)

#OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente o mesmo sera ignorado
# sem gerar erros e não fará parte do conjunto.

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)  # Duplicidade não gera erro, simplesmente não adiciona
s.add(4)
print(s)

# Remover elementos em um cojunto

# Forma 1 -
s = {1, 2, 3}
s.remove(3) # Não é indice e sim valor.
print(s)
# OBS: Caso o valor não seja encontrado, sera gerado o erro, KeyError.

# Forma 2 -
s.discard(2)
print(s)

# OBS: Se o valor não for encontrado nenhum erro é gerado

# Copiando um conjunto para outro...
# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - ShalowCopy
novo = s
novo.add(4)

print(novo)
print(s)

s = {1, 2, 3}

#podemos remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos matematicos em conjuntos.
estudantes_python = {'pessoa1','pessoa2','pessoa3','pessoa4'}
estudantes_java = {'pessoa2', 'pessoa4','pessoa1','pessoa7'}

# Veja que alguns alunos estudam nas duas.
# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando Union
unicos1 = estudantes_python.union(estudantes_java)
print("São estudantes unicos",unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em AMBOS os cursos
# Forma 1 - Utilizando o intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o & comercial
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes de um curso que não estão no outro

so_python = estudantes_python.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma, valor maximo, valor minimo, tamanho

# Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}
print(sum(s)) #Soma
print(max(s)) #Maior valor
print(min(s)) #Menos valor
print(len(s)) #QUantos elementos a no conjunto