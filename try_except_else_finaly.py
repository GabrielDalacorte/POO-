"""
Try / Except / Else / Finally

Dica de quando tratar código:
    -- TODA ENTRADA DEVE SER TRATADA!

# Else -> É executado somente se não ocorrer o erro.

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor Incorreto")
else:
    print(f'Você digitou {num}')  
      
  
# Finally

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor Incorreto")
else:
    print(f'Você digitou {num}')  
finally:
    print("Executando o finally")     

# OBS: O bloco finally é sempre executado. Independente se houve exceção ou não.

# O finally, geralmente é utilizado para fechar ou desalocar recursos.


# Exemplo mais complexo:

def dividir(a, b):
    return a / b

try:
    num1 = int(input("Informe o primeiro numero: "))
except ValueError:
    print("O valor precisa ser numérico")
    
try:
    num2 = int(input("Informe o segundo numero: "))
except ValueError:
    print("O valor precisa ser numérico")

try:
    print(dividir(num1, num2))
except NameError:
    print("Valor Incorreto")


# Exemplo mais complexo CORRETO
# OBS; Você é responsavel pelas entradas das susas funões. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Valor incorreto"
    except ZeroDivisionError:
        return "Impossivel dividir por Zero"
     
num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")
print(dividir(num1, num2))


# Exemplo mais complexo SEMI-GENERICO


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Valor incorreto: {err}"
     
num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")
print(dividir(num1, num2))

"""

