# 1.Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano Crie uma instância dessa classe e atribua valores aos seus atributos      

class Carro:
    carros = []

    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def listar_carros():
        print()
        print('=' * 40)
        print('Modelo'.ljust(14),'Cor'.ljust(15),'Ano')
        print('-' * 40)
        for carro in Carro.carros:
            print(f'{carro.modelo.ljust(15)}{carro.cor.ljust(15)}{carro.ano}')
            # print(f'Modelo: {carro.modelo}', f'Cor: {carro.cor}', f'Ano: {carro.ano}',sep='\n')

resp = 'S'
while resp == 'S':
    print('=' * 40)
    modelo = input('Qual modelo do carro: ').capitalize()
    cor = input('Qual a cor do carro: ').capitalize()
    ano = int(input('Qual o ano do carro: '))
    print('=' * 40)
    Carro(modelo,cor,ano) # <---- Instância

    resp = input('Deseja continuar? [S/N]: ').upper().strip()
    if resp == 'N':
        resp = 'N'

Carro.listar_carros()
print('=' * 40)

# 2.Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos Instancie um restaurante e atribua valores aos seus atributos

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    endereco = ''
    contato = int()

restaurante = Restaurante()
restaurante.nome = 'Slice tennis'
restaurante.categoria = 'Restaurante Esportivo'
restaurante.endereco = 'Alameda África, 619 - Colinas da Anhanguera, Santana de Parnaíba - SP'
restaurante.contato = 11971440538

print(f'Nome: {restaurante.nome}',f'Categoria: {restaurante.categoria}',f'Funcionamento: Ativo' if restaurante.ativo == True else 'Funcionamento: Inativo' ,f'Endereço: {restaurante.endereco}',f'Contato: {restaurante.contato}',sep='\n')

# 3.Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão Crie uma instância utilizando o construtor

class Restaurante:

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

informacoes_restaurante = Restaurante('Pedra Branca', 'Self-service') # Instância da classe
print(f'Nome Restaurante: {informacoes_restaurante.nome}',f'Categoria: {informacoes_restaurante.categoria}',f'Situação: Ativo' if informacoes_restaurante.ativo == True else 'Situação: Inativo',sep='\n')

# 4.Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria Exiba essa mensagem para uma instância de restaurante

class Restaurante:

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    def __str__(self):
        return f'Nome: {self.nome}\nCategoria: {self.categoria}'

informacao_restaurante = Restaurante('Pedra Branca', 'Self-Service')
print(informacao_restaurante)

# 5.Crie uma classe chamada Cliente e pense em 4 atributos Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor

class Cliente:
    def __init__(self,nome,peso,altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.imc = self.calcular_imc()

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)
    
    def __str__(self):
        return (
        f'Nome: {self.nome}\n'
        f'Peso: {self.peso}kg\n'
        f'Altura: {self.altura}m\n'
        f'Imc: {self.imc:.2f}'
        )

cliente = Cliente('Adamos', 115, 1.96)
print(cliente)
