"""
POO - Herança (Inheritance)

Ideia de Herança é a de reaproveitamento de código. Também para extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente 
    - Nome
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula 

Quando uma classe herda de outra classe, a classe herdade e conhecida por:
    [Pessoa]
    - Super classe;
    - Classe mae;
    - Classe pai;
    - Classe Base;
    - Classe Generica;

Quando uma classe herda de outra classe ela e chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Especifica;

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):  
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    #CLiente herda de pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        #Pessoa.__init__(self, nome, sobrenome, cpf) #Forma nao comum de acessar dados da super classe
        super().__init__(nome, sobrenome, cpf) # Forma comum de acessar dados da super classe
        self.__renda = renda

class Funcionario(Pessoa):
    #Funcionario herda de pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente("Gabriel", 'nunes', '879987850-04', '50000')
funcio1 = Funcionario("Braum", 'dalacorte', '989897787-03', '12344')

print(cliente1.nome_completo())
print(funcio1.nome_completo())

print(cliente1.__dict__)
print(funcio1.__dict__)

#Sobrescrita de metodos (Overriding)

Sobrescrita de metodos, ocorre quando reescrevemos/reimplementamos um metodos presente na super classe
em classes filhas.

"""
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):  
        return f'Nome completo: {self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # Forma comum de acessar dados da super classe
        self.__renda = renda

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # Caso eu queria mostrar o "nome_completo que esta em pessoa, mas queria mostra diferente"
    # e essa forma abaixo 
    def nome_completo(self):
        #print(super().nome_completo()) 
        #print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome} CPF: {self._Pessoa__cpf}'


#Sobrescrita de metodos (Overriding)

cliente1 = Cliente("Gabriel", 'nunes', '879987850-04', '50000')
funcio1 = Funcionario("Braum", 'dalacorte', '989897787-03', '12344')

print(cliente1.nome_completo())
print(funcio1.nome_completo())
