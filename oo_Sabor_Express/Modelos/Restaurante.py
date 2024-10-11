class Restaurante: # Classe + Atributos
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

# print(dir(restaurante_praca)) #dir = Exibe todas os atributos, métodos e propriedades de um self.
#vars = Mostra um dicionarios dos atributos e metodos, que foi os atributos passados no código anterior
print(restaurante_pizza)
print(restaurante_praca)


# class Musica:
#     nome = ''
#     artista = ''
#     duracao = float()

# musica_1 =  Musica()
# musica_1.nome = 'Lacrimosa - Warum so tief?'
# musica_1.artista = 'Tilo wolf'
# musica_1.duracao = 9.11

# print(f'Nome da música: {musica_1.nome}', f'Artista: {musica_1.artista}',f'Duração: {musica_1.duracao}', sep='\n')
