class Livro:

    livros = []  # Lista para armazenar os livros criados

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        Livro.livros.append(self)  # Adiciona o livro à lista da classe

    @property
    def descricao(self):
        """Retorna a descrição detalhada do livro."""
        return (f'Título: {self.titulo}\n'
                f'Autor: {self.autor}\n'
                f'Ano de publicação: {self.ano_publicacao}\n')

    @classmethod
    def adicionar_livro(cls, titulo, autor, ano_publicacao):
        """Cria um novo objeto Livro e o adiciona à lista."""
        novo_livro = cls(titulo, autor, ano_publicacao)
        return f'Livro "{novo_livro.titulo}" adicionado com sucesso!'

    @classmethod
    def listar_livros(cls):
        """Retorna a descrição de todos os livros armazenados."""
        if not cls.livros:
            return "Nenhum livro disponível."
        return '\n'.join([livro.descricao for livro in cls.livros])

# Criando livros com o método de classe
print(Livro.adicionar_livro('A Divina Comédia', 'Dante Alighieri', 2017))
print(Livro.adicionar_livro('Jesus Viveu na Índia', 'Holger Kersten', 2005))
print(Livro.adicionar_livro('Anhangá: A Fúria do Demônio', 'J. Modesto', 2008))

# Exibindo a lista completa de livros
print("\nLista de Livros:")
print(Livro.listar_livros())
