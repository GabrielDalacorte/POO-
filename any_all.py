"""
Any e All

All() -> Retorna True se todos os elementos do iterável, são verdadeiros ou ainda se o iteravel está
vazio.


# Exemplo all()

print(all([1, 2, 3, 4])) #Todos os números são verdadeiros? True
print(all([0, 1, 2, 3, 4])) #Todos os números são verdadeiros? False
print(all([])) #Todos os números são verdadeiros? True


nomes = ['Carlos', 'Camila'] 

print(all([nome[0] == 'C' for nome in nomes])) # ver se todos os usuarios que estão na lista, 
                                               #começam com a letra C


===================

Any() -> Retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vázio
retorna False.

print(any([1, 2, 3, 4])) # True
print(any([0, False, {}])) # False



all = Todos
any = Alguns
"""


