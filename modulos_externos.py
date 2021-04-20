"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

from colorama import init, Fore, Back
init()

print(Fore.RED + 'Gabriel Nunes')
print(Fore.MAGENTA + 'THasiane Dalacorte')
print(Back.GREEN + 'OIIOIOIO') # MT FEIO

"""

# CRIANDO PDF EM PYTHON

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'python pdf creation example!')
pdf.output('Primeiropdf.pdf', 'F')