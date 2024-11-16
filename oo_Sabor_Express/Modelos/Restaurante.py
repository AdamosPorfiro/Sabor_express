from Avaliação import Avaliacao
from Cardapio.Item_cardapio import ItemCardapio

'''Objeto resturante'''
class Restaurante: # Classe + Atributos
    '''Lista que armazena todos os restaurantes criados'''
    restaurantes = []

    '''Construtor que instância o objeto restaurante
    
    nome -> Nome do restaurante
    categoria -> Categoria que ele se encaixa
    avaliação -> Avaliação do cliente'''
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    '''Retorna uma fstring dos nomes dos restaurantes e suas categorias'''
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    '''Lista os restaurantes instanciados na lista
    Utilizamos loop for para interar dentro da lista com os objetos instanciados'''
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome'.ljust(18)} | {'Categoria'.ljust(18)} | {'Avaliações'.ljust(18)} | {'Status'}')
        print('-' * 50)
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(18)} | {restaurante._categoria.ljust(18)} | {str(restaurante.media_avaliacao).ljust(18)} | {restaurante.ativo}')
    
    '''Retorna string que definirá se o restaurante está ativo ou não'''
    @property #Um decorator(decorador) do python: Tem a capacidade de pegar um atributo, no nosso caso o ativo.
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    '''Altera o estado de um restaurante para ativo ou desativo'''
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    '''Recebe as avaliações do úsuario'''
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota > 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    '''Calcula e retorna uma media que é armazenada na lista'''
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma_das_nontas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_nontas / quantidade_de_notas, 1)
        return media

    def adicionar_item_no_cardapio(self, item):
            if isinstance(item, ItemCardapio):
                self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start = 1):
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)

