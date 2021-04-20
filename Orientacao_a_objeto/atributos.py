"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmico;

# Atributos de instância: São atributos declarados dentro do método construtor.
"""

# Classes com Atributos de Instância Público
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Classes com Atributos Prívados
class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.__email)
    
    # Ou pode mostrar os dois tambem
    #def mostra_tudo(self):
    #    print(self.__email, self.__senha)

# Exemplos
user = Acesso('user@gmail.com', '12132132')
#print(user.__email) #AttributeError
#print(dir(user))
#print(user._Acesso__email) # Temos acesso. Mas não deveriamos fazer este acesso.

user.mostra_senha()
user.mostra_email()
# user.mostra_tudo()

# Atributos de Classe


class Produto:

    #Atributo de classe
    imposto = 1.05
    contador = 0
    def __init__(self, nome, descricao, valor): # Geralmente somente os dados que vamos receber
        # Não botei o imposto nem contator pois eles são postos pelo proprio python e não por
        # alguem que vai executar o código
        self.id = Produto.contador + 1 #Pega o ID + CONTADOR + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto) # Valor * Imposto
        Produto.contador = self.id  # PRODUTO.CONTADOR É IGUAL A "ID"

p1 = Produto("Playstation 4", "Video Game", 2300)
p2 = Produto("XBOX One", "Video Game", 4500)
print(p1.valor)
print(p1.id)
print(p2.id)

# Não é comum utilizar atributos dinâmicos   
# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.
# OBS: O atributo dinâmico será exclusivo da instância que o criou.
p2.peso = '5kg' # Note que na classe Produto não exsiste o atributo peso
print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')