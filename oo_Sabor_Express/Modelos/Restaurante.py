class Restaurante: # Classe + Atributos
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

# print(dir(restaurante_praca)) #dir = Exibe todas os atributos, métodos e propriedades de um self.
#vars = Mostra um dicionarios dos atributos e metodos, que foi os atributos passados no código anterior
Restaurante.listar_restaurantes()


class Musica:
    musicas = []

    def __init__(self,nome,artista,duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'Nome da música: {musica.nome}\nNome do artista: {musica.artista}\nDuração da música: {musica.duracao} minutos') 

Musica('Lacrimosa - Warum so tief?', 'Tilo wolf', 9.11)
Musica.listar_musicas()
