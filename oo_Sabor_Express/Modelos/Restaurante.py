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
    
# print(dir(restaurante_praca)) #dir = Exibe todas os atributos, métodos e propriedades de um self.
#vars = Mostra um dicionarios dos atributos e metodos, que foi os atributos passados no código anterior
Restaurante.listar_restaurantes()

