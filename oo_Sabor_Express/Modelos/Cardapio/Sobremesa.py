from Cardapio.Item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    
    def __init__(self, nome, preco, descricao,tipo, tamanho):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao

    def __str__(self):
        return f'{self._nome}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.06)
