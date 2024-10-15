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
    Carro(modelo,cor,ano)

    resp = input('Deseja continuar? [S/N]: ').upper().strip()
    if resp == 'N':
        resp = 'N'

Carro.listar_carros()
print('=' * 40)

# 2.Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos Instancie um restaurante e atribua valores aos seus atributos

# 3.Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão Crie uma instância utilizando o construtor

# 4.Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria Exiba essa mensagem para uma instância de restaurante


# 5.Crie uma classe chamada Cliente e pense em 4 atributos Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor