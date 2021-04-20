"""
POO - Métodos

- Métodos(fu)

"""

class Lampada:
    def __init__(self, voltagem, luminosidade, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:
    contador = 4999
    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    #imposto = 1.05
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1 
        self.__nome = nome
        self.__valor = valor
        self.__descricao = descricao
        #self.valor = (valor * Produto.imposto) 
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o vaor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100   

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    """
    SO FAZEMOS OS 'DEF' ABAIXO  DA DEF__INIT__ QUANDO A NOSSA FUNÇÃO CRIADA FOR UTILIZAR
    ALGUM SELF."nOME" QUE TEM NO __INIT__. cASO QUEIRA CRIAR UMA DEF QUE NAO IRA USAR 
    O SELF QUE ESTA NO __INIT__ PODE CRIAR EM CIMA COM A DECORAÇÃO @CLASSMETHOD
    """

    @classmethod # Método de Classe
    def conta_usuarios(cls): # 'cls' == classe
        print(f'Temos {cls.contador} usuario(s) no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        # Rounds é para embaralhar a senha - Para melhorar a segurança
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def chega_senha(self, senha):
        if cryp.verify(senha, self.__senha): # Se senha criptografada for igual a senha, self.__senha
            # retorna true, se não retorna false
            return True
        return False

    def __gera_usuario(self): # método privado
        return self.__email.split('@')[0]

#p1 = Produto("PLaystations 4", "video game", 3400)
#print(p1.desconto(20)) #Valor do PS4 com 20% de desconto

#user1 = Usuario('Gabriel', 'Nunes', 'uerhrue@gmail.com', '3738743')
#print(user1.nome_completo())
#print(dir(user1))
#print(f'Senha User 1: {user1._Usuario__senha}') #Acessando de forma errada de um atributo de classe

'''
nome = input("Informe nome: ")
sobrenome = input("Informe o sobrenome: ")
email = input("Informe o e-mail: ")
senha = input("Informe a senha: ")
confirma_senha = input("Confirme a senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print("Senha não confere..")
    exit(1)

print("Usuario criado com sucesso.")

senha = input("Informe a senha para acesso: ")

if user.chega_senha(senha):
    print("Acesso permitido")
else:
    print('Acesso negado')

print(f'senha user Criptografada: {user._Usuario__senha}') #Acesso errado
'''

# Métodos de Classe

#user = Usuario("Gabriel", "Nunes", "gnuens.servico@gmail.com", "123456")
#Usuario.conta_usuarios() # Forma correta
#user.conta_usuarios() # Possível, mas incorreto

#user = Usuario("Gabriel", "Nunes", "gnuens.servico@gmail.com", "123456")

