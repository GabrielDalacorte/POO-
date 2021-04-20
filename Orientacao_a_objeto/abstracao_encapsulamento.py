"""
POO - Abstração e Encapsulamento 

"""

class Conta:
    contador = 400
     
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo}, do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor precisa ser positivo")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print("Saldo insuficiente")
        else:
            print('O valor deve ser positivo')       

    def transferir(self, valor, conta_destino):
        # Remover valor da conta origem
        self.__saldo -= valor

        # Adicionando  o valor na conta destino
        conta_destino.__saldo += valor
         

# Testando
conta1 = Conta("Geek", 150.00, 1500)
conta2 = Conta("Gabriel", 2150.00, 11500)
conta1.extrato()
conta2.extrato()

conta2.transferir(1030, conta1)
conta1.extrato()
conta2.extrato()
#conta1.depositar(150)
#print(conta1.__dict__)
#conta1.sacar(100)
#conta1.sacar(1000) #Saldo insuficiente                   
#print(conta1.__dict__)
#conta1.extrato()

#print(conta1._Conta__titular) # Name Manglin - MANEIRA ERRADA