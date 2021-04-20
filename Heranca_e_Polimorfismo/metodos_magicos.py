"""
POO - Metodos Magicos

Metodos magicos sao todos os metodos que utilizam dunder.

dunder init -> __init__

Dunder > Double Underscore ( Dois underline - __init__ )

dunder repr -> __repr__ (MENOS USADO)
    * Representacao do objeto
    * Geralmenteo usada pelo desenvolvedor para ver o resultado final

    def __repr__(self): #__repr__ fazer a representacao do nosso objeto
        return f'Titulo: {self.titulo} \nAutor: {self.autor} \nPaginas: {self.paginas}'

dunder str -> __str__ (MAIS USADO)
    * Geralmente usada para mostrar os resultados.
        def __str__(self):
        return f'Titulo: {self.titulo} \nAutor: {self.autor} \nPaginas: {self.paginas}'

dunder len -> __len__ 
    * Usado para trazer o numero de algo
    
    def __len__(self):
        return self.paginas


    print(len(livro2))

"""
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'Titulo: {self.titulo} \nAutor: {self.autor} \nPaginas: {self.paginas}'

    def __len__(self):
        return self.paginas

    def __del__(self): #Eu nao curti muito esse aqui.
        print('Um objeto do tipo livro foi deletado da memoria')
    
    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro): #Multiplicacao - Self(livro) outro(numero)
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Nao posso multiplicar'


#livro1 = Livro("A branca de Neve", 'Branca', 320)
livro2 = Livro("PYthon", 'Geek University', 400)

#print(livro1)
#print(livro2)

#print(len(livro2))
#print(livro2 + livro1)

print(livro2 * 3)