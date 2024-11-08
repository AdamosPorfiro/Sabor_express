# 1.Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

class Livro:

    livros = []
    def __init__(self,titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    
        
# 2.Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

    def __str__(self):
        return f'\nTitulo: {self.titulo}\nAutor: {self.autor}\nAno de publicação: {self.ano_publicacao}'

livro_1 = Livro('A divina comédia', 'Dante Alighieri', 1321)
livro_2 = Livro('Anhangá: a Fúria do Demônio', 'J. Modesto', 2008)

print(f'{livro_1}\n{livro_2}')

3.Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

    def __str__(self):
        return f'\nTitulo: {self.titulo}\nAutor: {self.autor}\nAno de publicação: {self.ano_publicacao}\nStatus: {'Disponível' if self.disponivel else 'Indisponível'}'

    def emprestar(disponivel):
        disponivel.disponivel = False

livro_1 = Livro('A divina comédia', 'Dante Alighieri', 1321)
Livro.emprestar(livro_1)
livro_2 = Livro('Anhangá: a Fúria do Demônio', 'J. Modesto', 2008)

print(f'{livro_1}\n{livro_2}')

# 4.Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

class Livro:

    livros = []
    def __init__(self,titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)
    
    @staticmethod
    def verificar_disponibilidade(ano):
        livro_disponivel_ano = [
            livro.titulo for livro in Livro.livros
            if livro.ano_publicacao == ano and livro.disponivel
        ]
        return livro_disponivel_ano
    @classmethod
    def listar_livros(cls):
        for livro in cls.livros:
            print(f'\nTitulo: {livro.titulo}\nAutor: {livro.autor}\nAno de publicação: {livro.ano_publicacao}\nDisponibilidade:',f'Disponível' if livro.disponivel == True else 'Indisponivel')

livro_1 = Livro('A divina comédia', 'Dante Alighieri', 1321)
livro_2 = Livro('Anhangá: a Fúria do Demônio', 'J. Modesto', 2008)
livro_3 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)

ano_do_livro = 2008
livros_disponiveis_2008 = Livro.verificar_disponibilidade(ano_do_livro)
print(f'Livros disponiveis em {ano_do_livro}: {livros_disponiveis_2008}')
        
# 5.Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

class Livro:

    livros = []
    def __init__(self,titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)
    
    @classmethod
    def listar_livros(cls):
        for livro in cls.livros:
            print(f'\nTitulo: {livro.titulo}\nAutor: {livro.autor}\nAno de publicação: {livro.ano_publicacao}\nDisponibilidade:',f'Disponível' if livro.disponivel == True else 'Indisponivel')

Esta na pasta Biblioteca.py
from Atividade_metodos_construtores_classes_ import Livro

livro_1 = Livro('A divina comédia', 'Dante Alighieri', 1321)
livro_2 = Livro('Anhangá: a Fúria do Demônio', 'J. Modesto', 2008)
livro_3 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)

def main():
    Livro.listar_livros()

if __name__ == '__main__':
    main()

# 6.No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

class Livro:

    livros = []
    def __init__(self,titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    @classmethod
    def listar_livros(cls):
        for livro in cls.livros:
            print(f'\nTitulo: {livro.titulo}\nAutor: {livro.autor}\nAno de publicação: {livro.ano_publicacao}\nDisponibilidade:',f'Disponível' if livro.disponivel == True else 'Indisponivel')
    
    def emprestar(disponivel):
        disponivel.disponivel = False

Esta na pasta Biblioteca.py
from Atividade_metodos_construtores_classes_ import Livro

livro_1 = Livro('A divina comédia', 'Dante Alighieri', 1321)
livro_2 = Livro('Anhangá: a Fúria do Demônio', 'J. Modesto', 2008)
livro_3 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)

def main():
    Livro.emprestar(livro_1)
    Livro.listar_livros()

if __name__ == '__main__':
    main()

# 7.No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

class Livro:

    livros = []
    def __init__(self,titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)
    
    @staticmethod
    def verificar_disponibilidade(ano):
        livro_disponivel_ano = [
            livro.titulo for livro in Livro.livros
            if livro.ano_publicacao == ano and livro.disponivel
        ]
        return livro_disponivel_ano
    
    @classmethod
    def listar_livros(cls):
        for livro in cls.livros:
            print(f'\nTitulo: {livro.titulo}\nAutor: {livro.autor}\nAno de publicação: {livro.ano_publicacao}\nDisponibilidade:',f'Disponível' if livro.disponivel == True else 'Indisponivel')
    
    def emprestar(disponivel):
        disponivel.disponivel = False

#Esta na pasta Biblioteca.py
from Atividade_metodos_construtores_classes_ import Livro

livro_1 = Livro('A divina comédia', 'Dante Alighieri', 1321)
livro_2 = Livro('Anhangá: a Fúria do Demônio', 'J. Modesto', 2008)
livro_3 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)

def main():
    Livro.listar_livros()
    ano_do_livro = 2008
    livros_disponiveis_2008 = Livro.verificar_disponibilidade(ano_do_livro)
    print(f'\nLivros disponiveis do ano de {ano_do_livro}: {livros_disponiveis_2008}')

if __name__ == '__main__':
    main()
    
# 8.Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

class Livro:

    livros = []
    def __init__(self,titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)
    
    def __str__(self):
        return f'\nTitulo: {self.titulo}\nAutor: {self.autor}\nAno de publicação: {self.ano_publicacao}\nStatus: {'Disponível' if self.disponivel == True else 'Indisponível'}'

#Está na pasta main.py detro de biblioteca.py
from Atividade_metodos_construtores_classes_ import Livro

livro_1 = Livro('A divina comédia', 'Dante Alighieri', 1321)
livro_2 = Livro('Anhangá: a Fúria do Demônio', 'J. Modesto', 2008)

def main():
    print(f'{livro_1}\n\n{livro_2}')

if __name__ == '__main__':
    main()