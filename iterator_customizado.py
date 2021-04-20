"""
Escrevendo um iterator customizado.


for n in range(5, 11): #Comeca no 5 e vai ate 10
    print(n)

"""
class Contador: # Faz a mesma coisa que um rage so que com orientação a objeto
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

for n in Contador(1, 61):
    print(n)
'''
con = Contador(1, 61)

it = iter(con)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
'''