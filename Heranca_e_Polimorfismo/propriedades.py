"""
POO - Propriedades - Properties

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        Conta.contador += 1

    def extrato(self):
        return f'{self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    #Get significa "PEGAR"
    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Gabriel', 3000, 5000)
conta2 = Conta('Thasiane', 4000, 6000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()

#soma = conta1._Conta__saldo + conta2._Conta__saldo #Forma nao recomendada para fazer essa soma
print(f'A soma do saldo das conta e {soma}') 

print(conta1.__dict__)
conta1.set_limite(999999)
print(conta1.__dict__)

===================== UTILIZANDO PROPRIEDADES ===========================================
"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        Conta.contador += 1
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter # -> Seria o "def set_limite"
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'{self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
    



conta1 = Conta('Gabriel', 3000, 5000)
conta2 = Conta('Thasiane', 4000, 6000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(soma)

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)
print(conta1.limite)

print(conta1.valor_total)
print(conta2.valor_total)