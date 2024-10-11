# 1.Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano Crie uma instância dessa classe e atribua valores aos seus atributos      

# 2Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos Instancie um restaurante e atribua valores aos seus atributos

# 3Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão Crie uma instância utilizando o construtor

class Restaurante():
    
    def __init__(,nome,categoria,cardapio,preco):
        nome = nome
        categoria = categoria
        ativo = False
        cardapio = cardapio
        preco = preco

    def __str__():
        return f'Nome: {nome}\nCategoria: {categoria}\nCardapio: {cardapio}\nPreço: R$ {preco} | {ativo}'

restaurante = Restaurante('Slice Tennis', 'Comida Típica', 'Arroz c/ feijão e bife acebolado', 2350)

print(restaurante)

# 4Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria Exiba essa mensagem para uma instância de restaurante


# 5Crie uma classe chamada Cliente e pense em 4 atributos Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor