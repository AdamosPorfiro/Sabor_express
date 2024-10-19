# 1.Gerenciamento de Estoque:

# Crie uma classe Produto que tenha atributos nome, preco e quantidade.
# Implemente um método de classe criar_a_partir_nome que receba apenas um nome e retorne um objeto Produto com preco e quantidade padrão (por exemplo, 10.0 e 0).
# Adicione uma propriedade valor_total_estoque que retorne o valor total do estoque (preco * quantidade).

class Produto:

    produtos = []
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        Produto.produtos.append(self)

    @classmethod
    def criar_a_partir_nome(cls,nome):
        return cls(nome, preco = 9.90, quantidade = 0)
    
    @classmethod
    def listar_produtos(cls):
        print()
        print(f'{'Nome'.ljust(18)} | {'Preço'.ljust(18)} | {'Quantidade'.ljust(18)} | {'Valor Total'}')
        print('-' * 80)
        for produto in cls.produtos:
            print(f'{produto.nome.ljust(18)} | {produto.preco} {''.ljust(14)} | {produto.quantidade}{''.ljust(17)} | {produto.valor_total_estoque:.2f}')
    
    @property
    def valor_total_estoque(self):
        return self.preco * self.quantidade
    
produto_1 = Produto.criar_a_partir_nome('Garrafa')
produto_2 = Produto.criar_a_partir_nome('Lapis de cor')
Produto.listar_produtos()

# 2.Gestão de Carros em uma Concessionária:

# Crie uma classe Carro que tenha os atributos marca, modelo, ano e quilometragem.
# Adicione um método de classe carro_zero_km que crie um carro com quilometragem igual a 0.
# Adicione uma propriedade idade que calcule a idade do carro com base no ano atual.

from datetime import datetime
class Carro:

    carros = []
    def __init__(self,marca,modelo,ano,quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem
        Carro.carros.append(self)

    @classmethod
    def carro_zero_km(cls, marca, modelo, ano):
        return cls(marca, modelo, ano, quilometragem=0)

    @property
    def idade(self):
        return datetime.now().year - self.ano
    
carro1 = Carro("Toyota", "Corolla", 2019, 30000)
print(f"Idade do {carro1.marca} {carro1.modelo}: {carro1.idade} anos")

