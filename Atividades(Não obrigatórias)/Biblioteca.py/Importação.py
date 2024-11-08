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