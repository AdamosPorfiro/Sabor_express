# 5- Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

from Exercicio_2 import Veiculo

class Moto(Veiculo):

    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

# 6- Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.
    
    def __str__(self):
        return f'\n\nMarca: {self._marca}\nModelo: {self._modelo}\nTipo da moto: {'Esportiva' if self._tipo == 'Esportiva' else 'Casual'}'