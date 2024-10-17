class Restaurante: # Classe + Atributos
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome'.ljust(18)} | {'Categoria'.ljust(18)} | {'Status'}')
        print('-' * 50)
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(18)} | {restaurante._categoria.ljust(18)} | {restaurante.ativo.ljust(18)}')
    
    @property #Um decorator(decorador) do python: Tem a capacidade de pegar um atributo, no nosso caso o ativo.
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
restaurante_praca = Restaurante('praça','gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza Express', 'italiana')

# print(dir(restaurante_praca)) #dir = Exibe todas os atributos, métodos e propriedades de um self.
#vars = Mostra um dicionarios dos atributos e metodos, que foi os atributos passados no código anterior
Restaurante.listar_restaurantes()


# class Musica:
#     musicas = []

#     def __init__(self,nome,artista,duracao):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao
#         Musica.musicas.append(self)
    
#     def listar_musicas():
#         for musica in Musica.musicas:
#             print(f'Nome da música: {musica.nome}\nNome do artista: {musica.artista}\nDuração da música: {musica.duracao} minutos') 

# Musica('Lacrimosa - Warum so tief?', 'Tilo wolf', 9.11)
# Musica.listar_musicas()
