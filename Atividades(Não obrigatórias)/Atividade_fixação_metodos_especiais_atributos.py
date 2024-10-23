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
    
    @classmethod
    def listar_carros(cls):
        for carro in cls.carros:
            print(f'Idade do {carro.marca} {carro.modelo} é: {carro.idade} anos')

    @property
    def idade(self):
        return datetime.now().year - self.ano
    
carro1 = Carro("Toyota", "Corolla", 2019, 30000)
carro2 = Carro("Volkswagen", "Gol", 2003, 132482)
print()
Carro.listar_carros()

# 3.Contador de Instâncias Criadas:

# Crie uma classe Animal que tenha um atributo nome.
# Adicione um contador de instâncias criadas. Use um @classmethod para manter e acessar o número de instâncias criadas.
# Implemente uma propriedade descricao que retorne uma string como "Animal: [nome]".

class Animal:
    
    lista_de_animais = []
    contador = 0
    def __init__(self,nome):
        self.nome = nome
        Animal.lista_de_animais.append(self)
        Animal.contador += 1
    
    @classmethod
    def animais_criados(cls):
        print()
        print(f'Foram criados: {cls.contador} instâncias para animais')
        for i in cls.lista_de_animais:
            print(f'{i.descricao}')
    
    @property
    def descricao(self):
        return f'Animal: {self.nome}'

animal_1 = Animal('Girafa')
animal_2 = Animal('Cachorro')
animal_3 = Animal('Gato')

Animal.animais_criados()

# 4.Conversão de Moedas:

# Crie uma classe Moeda com atributos nome e taxa_conversao (por exemplo, de dólar para reais, a taxa pode ser 5.0).
# Adicione um método de classe a_partir_de_taxa que crie uma moeda a partir de uma taxa de conversão especificada.
# Adicione uma propriedade taxa_em_reais que retorne quanto vale 1 unidade dessa moeda em reais.

class Moeda:

    def __init__(self, nome, taxa_conversao):
        self.nome = nome
        self.taxa_conversao = taxa_conversao

    @classmethod
    def a_partir_de_taxa(cls,nome,taxa_conversao):
        return cls(nome, taxa_conversao)
    
    def imprimir_dados(self):
        print(f'\nA taxa de conversão de um {self.nome} é de R$ {self.taxa_conversao} reais.')
    
    @property
    def taxa_em_reais(self):
        return self.taxa_conversao
    
moeda_dollar = Moeda.a_partir_de_taxa('Dolar', 5)
moeda_dollar.imprimir_dados()
# print()
# print(f'Moeda: {moeda_dollar.nome}')
# print(f'A taxa de conversão de um {moeda_dollar.nome} é de R$ {moeda_dollar.taxa_conversao} reais ')

# 5. Sistema de Cadastro de Estudantes:
# Crie uma classe Estudante com atributos como nome, idade e curso. Adicione um método de classe cadastrar que receba as informações de um estudante e retorne um objeto Estudante. Implemente uma propriedade que retorne uma descrição do estudante, incluindo o nome, idade e curso.

class Estudante:

    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    @classmethod
    def cadastrar(cls,nome,idade,curso):
        cls.cadastrar('Adamos',30,'Ciência da computação')

    @property
    def descricao(self):
        return print(f'Aluno: {self.nome}\nIdade: {self.idade}\nCurso:{self.curso}')
    
print()
# 6. Controle de Funcionários:
# Crie uma classe Funcionario com atributos nome, cargo e salario. Adicione um método de classe criar_por_cargo que recebe um cargo e cria um funcionário com um salário padrão. Adicione uma propriedade que calcule o salário anual (salário mensal multiplicado por 12).

# 7. Sistema de Reservas de Hotel:
# Crie uma classe Quarto que tenha atributos como numero, tipo (simples, duplo, suíte) e disponibilidade. Adicione um método de classe reservar_quarto que receba o número do quarto e retorne uma mensagem de confirmação. Implemente uma propriedade que retorne o status do quarto (disponível ou não).

# 8. Sistema de Cadastro de Livros:
# Crie uma classe Livro com atributos como titulo, autor e ano_publicacao. Adicione um método de classe adicionar_livro que receba as informações do livro e retorne um objeto Livro. Implemente uma propriedade que retorne uma descrição do livro, incluindo título, autor e ano de publicação.

# 9. Gestão de Pedidos em um Restaurante:
# Crie uma classe Pedido com atributos cliente, itens (uma lista de itens do pedido) e valor_total. Adicione um método de classe criar_pedido que receba o nome do cliente e uma lista de itens. Calcule o valor total do pedido. Implemente uma propriedade que retorne a descrição do pedido.

# 10. Sistema de Registro de Atividades Físicas:
# Crie uma classe Atividade com atributos nome, duracao (em minutos) e calorias. Adicione um método de classe registrar_atividade que receba as informações da atividade e retorne um objeto Atividade. Implemente uma propriedade que calcule a queima de calorias por minuto.