from Cardapio.Item_cardapio import ItemCardapio

'''Herança'''
class Bebida(ItemCardapio):

    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self) -> str:
        return f'{self._nome}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)