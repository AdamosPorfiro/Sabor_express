class Restaurante: # Classe + Atributos
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

# print(dir(restaurante_praca)) #dir = Exibe todas os atributos, métodos e propriedades de um objeto.
print(vars(restaurante_praca)) #vars = Mostra um dicionarios dos atributos e metodos, que foi os atributos passados no código anterior

class Musica:
    nome = ''
    artista = ''
    duracao = float()

musica_1 =  Musica()
musica_1.nome = 'Lacrimosa - Warum so tief?'
musica_1.artista = 'Tilo wolf'
musica_1.duracao = 9.11

print(f'Nome da música: {musica_1.nome}', f'Artista: {musica_1.artista}',f'Duração: {musica_1.duracao}', sep='\n')
