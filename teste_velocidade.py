"""
Teste de Velocidade com Expressões Geradoras


"""

# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(ge1) #Generator
print(next(ge1))
print(next(ge1))

# Generator Expression
ge2 = (num for num in range(1, 10))

print(ge2)
print(next(ge2))
print(next(ge2))