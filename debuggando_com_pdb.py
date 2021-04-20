"""
Debugando com PDB

PDB -> Python Debugger

"""

# Existem formas profissionais de fazer esse 'debug', utilizando o debugger
# Em python, podemos fazer isso em diferentes IDEs, com PyCharm ou utilizando
# o PDB - Python Debugger

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Valor incorreto: {err}"
     
print(dividir(1, 5))