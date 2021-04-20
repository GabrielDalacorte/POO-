"""
Modulo Collections - Default Dict

Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um
valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default sera atribuido.

OBS: Lambdas são funções sem nome, que podem ou não receber parametros de entrada
e retornar valores.
"""

from collections import defaultdict
dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Prog em Python:Essensial'
print(dicionario['outro']) #KeyError: no dicionario comum, mas aqui não...
print(dicionario)