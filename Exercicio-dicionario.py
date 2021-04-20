listAlunos = {}

NewAluno = input("Nome do aluno: ")
Nota1 = float(input("Nota 1: "))
Nota2 = float(input("Nota 2: "))
resultado = (Nota1 + Nota2) / 2
print(resultado)
listAlunos[NewAluno] = resultado

for indice, chave in enumerate(listAlunos):
    print(f'{indice} = Nome: {chave}: \n Nota: {listAlunos[chave]}')
