"""
Geradores

- Geradores (Generators) são Iterators (Iteradores); 

OBS: O contrario não é verdadeiro. Ou seja, nem todo itereitor é um generator.

Outras informações:
    - Generators podem ser criados com funções geradoras;
    - Funções geradoras utilizam a palavra reservada yield;
    - Generators podem ser criados com expressoes geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras) 

----------------------------------------------------------------------------------
| Funções                                | Generator Functions                   |
----------------------------------------------------------------------------------
| Utilizam return                        | utilizam yield                        |
----------------------------------------------------------------------------------
| retorna uma vez                        | podem utilizar yield multiplas vezes  | 
----------------------------------------------------------------------------------
| quando executada, retorna um valor     | quando executada, retorna um generator|
----------------------------------------------------------------------------------
"""

# Exemplo Função Geradora (Generator Function)  

def conta_at(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

#OBS: Uma Generator Function não é um generator. Ela gera um generator.

gen = conta_at(10)
#print(type(gen))

for num in gen:
    print(num)
    
