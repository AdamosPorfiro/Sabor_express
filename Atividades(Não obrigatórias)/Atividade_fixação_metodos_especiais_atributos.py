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

# 5. Sistema de Cadastro de Estudantes:
# Crie uma classe Estudante com atributos como nome, idade e curso. Adicione um método de classe cadastrar que receba as informações de um estudante e retorne um objeto Estudante. Implemente uma propriedade que retorne uma descrição do estudante, incluindo o nome, idade e curso.

class Estudante:

    estudantes = {}

    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        Estudante.estudantes[self.nome]= {
            'Idade' : self.idade, 
            'Curso' : self.curso
        }
    
    @classmethod
    def cadastrar(cls,nome,idade,curso):
        return cls(nome, idade, curso)
    
    @classmethod
    def listar_alunos(cls):
        for nome, dados in cls.estudantes.items():
            estudante = cls(nome, dados['Idade'], dados['Curso'])
            print(estudante.descricao)
    

    @property
    def descricao(self):
        return f'\nAluno: {self.nome}\nIdade: {self.idade}\nCurso:{self.curso}\n'
    
resp = 'S'
while resp == 'S':
    nome = input('\nNome: ')
    idade = int(input('Idade: '))
    curso = input('Curso: ')
    Estudante.cadastrar(nome, idade, curso)

    resp = input('Deseja cadastrar mais alunos? [S/N]: ').upper().strip()
    if resp == 'N':
        break

Estudante.listar_alunos()

# 6. Controle de Funcionários:
# Crie uma classe Funcionario com atributos nome, cargo e salario. Adicione um método de classe criar_por_cargo que recebe um cargo e cria um funcionário com um salário padrão. Adicione uma propriedade que calcule o salário anual (salário mensal multiplicado por 12).

class Funcionarios:

    dados_de_cada_funcionario = {}

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.adicionar_funcionario()
    
    def adicionar_funcionario(self):
        if self.cargo not in Funcionarios.dados_de_cada_funcionario:
            Funcionarios.dados_de_cada_funcionario[self.cargo] = []
        Funcionarios.dados_de_cada_funcionario[self.cargo].append(self)
           
    @classmethod
    def criar_por_cargo(cls,nome,cargo):
        salario_padrao = 3000
        return cls(nome, cargo, salario_padrao)
    
    @classmethod
    def listar_funcionarios(cls):
        for cargo, funcionarios in cls.dados_de_cada_funcionario.items():
            print(f'\nCargo: {cargo}')
            for funcionario in funcionarios:
                print(  f'Funcionario: {funcionario.nome}'
                        f'\nSalario: {funcionario.salario}'
                        f'\nSalario anual: {funcionario.calculo_salario_anual}\n'
                      )
                
    
    @property
    def calculo_salario_anual(self):
            return self.salario * 12
    
Funcionarios.criar_por_cargo('Adamos', 'Porteiro')
Funcionarios.criar_por_cargo('Antonio', 'Vigilante')
Funcionarios.criar_por_cargo('Vilma', 'Porteiro')
Funcionarios.listar_funcionarios()



# 7. Sistema de Reservas de Hotel:
# Crie uma classe Quarto que tenha atributos como numero, tipo (simples, duplo, suíte) e disponibilidade. Adicione um método de classe reservar_quarto que receba o número do quarto e retorne uma mensagem de confirmação. Implemente uma propriedade que retorne o status do quarto (disponível ou não).

class Quarto:

    quartos = []
    def __init__(self, numero, tipo ,disponibilidade):
        self.numero = numero
        self.tipo = tipo
        self.disponibilidade = disponibilidade
        Quarto.quartos.append(self)
    
    #Verificando cada atributo de classe armazenado na lista
    # def __repr__(self):
    #     status = "Disponível" if self.disponibilidade else "Indisponível"
    #     return f"Quarto {self.numero} ({self.tipo}): {status}"

    @classmethod
    def reserva_quarto(cls):
        mensagem = ''
        for quarto in cls.quartos:
            mensagem += f'Numero do quarto: {quarto.numero}\n'
            mensagem += f'Tipo: {quarto.tipo}\n'
            mensagem += f'Status: {quarto.status}\n\n'
        return mensagem
    
    @property
    def status(self):
        return f'{'Disponível!' if self.disponibilidade else 'Indisponível!'}'
    
#Alimentar os atributos da classe
quarto_simples = Quarto(1, 'Simples', True)
quarto_duplo = Quarto(2, 'Duplo', False)
quarto_suite = Quarto(3, 'Suíte', True)

print(Quarto.reserva_quarto())


# 8. Sistema de Cadastro de Livros:
# Crie uma classe Livro com atributos como titulo, autor e ano_publicacao. Adicione um método de classe adicionar_livro que receba as informações do livro e retorne um objeto Livro. Implemente uma propriedade que retorne uma descrição do livro, incluindo título, autor e ano de publicação.

class Livro:

    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        Livro.livros.append(self)

    @property
    def descricao(self):
        return (f'Titulo: {self.titulo}\n'
                f'Autor: {self.autor}\n'
                f'Ano de publicação: {self.ano_publicacao}\n\n')
    
    @classmethod
    def adicionar_livro(cls,titulo,autor,ano_publicacao):
        novo_livro = cls(titulo,autor,ano_publicacao)
        return f'Livro {novo_livro.titulo} adicionado com sucesso!'
      
    @classmethod
    def listar_livros(cls):
        if not cls.livros:
            return 'Não existe livros disponíveis'
        return '\n'.join([livro.descricao for livro in cls.livros])

livro_1 = Livro.adicionar_livro('A divina comédia', 'Dante Alighieri', 2017)
livro_2 = Livro.adicionar_livro('Jesus viveu na índia', 'Holger Kersten', 2005)
livro_2 = Livro.adicionar_livro('Anhangá: A furia do demônio', 'J. Modesto', 2008)

print(Livro.listar_livros())

# 9. Gestão de Pedidos em um Restaurante:
# Crie uma classe Pedido com atributos cliente, itens (uma lista de itens do pedido) e valor_total. Adicione um método de classe criar_pedido que receba o nome do cliente e uma lista de itens. Calcule o valor total do pedido. Implemente uma propriedade que retorne a descrição do pedido.

class Pedido:

    pedidos = []
    def __init__(self,cliente,itens,valor_total):
        self.cliente = cliente
        self.itens = itens
        self.valor_total = valor_total
        Pedido.pedidos.append(self)
    
    @property
    def descricao(self):
        itens_formatados = '\n'.join([f'{item}: R$ {preco:.2f}' for item, preco in self.itens.items()])
        return (f'Cliente: {self.cliente}\n'
                f'Itens: {itens_formatados}\n'
                f'Valor total: R${self.valor_total:.2f}\n\n')
        

    @classmethod
    def criar_pedido(cls, cliente, itens):
        valor_pedido = sum(itens.values())
        novo_pedido = cls(cliente,itens,valor_pedido)
        return novo_pedido
    
    @classmethod
    def listando_pedidos(cls):
        if not cls.pedidos:
            return 'Não possoi nenhum livro disponível'
        return f'\n'.join([pedido.descricao for pedido in cls.pedidos])
    
item_1 = {'Prato simples' : 22.50, 'Refrigerante' : 5.99, 'Suco' : 3.99}
item_2 = {'Combo lanche' : 12.5, 'Batata grande' : 6, 'Refrigerante pq' : 4.99}
pedido_1 = Pedido.criar_pedido('Adamos', item_1)
pedido_2 = Pedido.criar_pedido('Alesson', item_2)

print(pedido_1.listando_pedidos())

# 10. Sistema de Registro de Atividades Físicas:
# Crie uma classe Atividade com atributos nome, duracao (em minutos) e calorias. Adicione um método de classe registrar_atividade que receba as informações da atividade e retorne um objeto Atividade. Implemente uma propriedade que calcule a queima de calorias por minuto.

class Atividade:

    atividades = []
    def __init__(self, nome, duracao, calorias):
        self.nome = nome
        self.duracao = duracao
        self.calorias = calorias
        Atividade.atividades.append(self)

    @classmethod
    def registrar_atividade(cls, nome, duracao, calorias):
        return cls(nome, duracao, calorias)
    
    @property
    def queima_de_calorias_por_minuto(self):
        if self.calorias == 0:
            return 0
        return self.calorias / self.duracao
    
    def mostrar_dados(self):
        return (f'Nome: {self.nome}\n'
                f'Duração: {self.duracao} minutos\n'
                f'Calorias: {self.calorias} Kcal\n'
                f'Calorias por minuto: {self.queima_de_calorias_por_minuto:.2f} \n\n')
    
    @classmethod
    def mostrar_todas_as_atividade(cls):
        if not cls.atividades:
            return 'Nenhuma atividade registrada!'
        return '\n'.join([atividade.mostrar_dados() for atividade in cls.atividades])
    
dados_exercicio_1 = Atividade.registrar_atividade('Corrida leve', 30, 350)
dados_exercicio_2 = Atividade.registrar_atividade('Musculação', 60, 800)

print(Atividade.mostrar_todas_as_atividade())

# 11. Sistema de Gestão de Clientes
# Crie uma classe Cliente que tenha atributos nome, email e telefone. Adicione um método de classe cadastrar_cliente que receba as informações de um cliente e retorne um objeto Cliente. Implemente uma propriedade que retorne a descrição do cliente.

class Cliente:

    clientes = [] # Lista com os objetos
    def __init__(self, nome, email, telefone): # Construtor com os parametros a serem preenchidos.
        self.nome = nome # Atributo do objeto
        self.email = email # Atributo do objeto
        self.telefone = telefone # Atributo do objeto
        Cliente.clientes.append(self) # Armazena os atributos e seus valores

    @classmethod # Metodo de classe
    def cadastrar_cliente(cls, nome, email, telefone): # Cria um objeto único
        return cls(nome, email, telefone) # Retorna esse objeto com seus atributos
    
    @property # Propriedade
    def descricao(self): # Que irá ter a descrição com os valores(atributos) do objeto
        return (f'Nome: {self.nome}\n' # Descrição com os atributos
                f'Email: {self.email}\n' # Descrição com os atributos
                f'Telefone: {self.telefone}\n\n') # Descrição com os atributos

    @classmethod #Metodo de classe
    def mostrar_todos_clientes(cls): # Vai mostrar todos os clientes da lista
        if not cls.clientes: # Caso não tenha cliente na lista retornará a string 
            return 'Nenhuma cliente cadastrado!' # string ou a seguir
        return '\n'.join([cliente.descricao for cliente in cls.clientes]) # Um for que irá entrar a lista e retornar a string formatada conforme a descrição 

cliente_1 = Cliente.cadastrar_cliente('Adamos', 'adamos.contato@gmail.com', 11986772188) # Atributo de classe (Adicionando valor ao objeto)
cliente_2 = Cliente.cadastrar_cliente('Thiago', 'adamos.sumeriios@gmail.com', 11945687214) # Atributo de classe (Adicionando valor ao objeto)

print(Cliente.mostrar_todos_clientes()) # Irá retornar a string conforme os dados da classe!

# 12. Controle de Tarefas
# Crie uma classe Tarefa com atributos titulo, descricao e status (pode ser "pendente" ou "concluída"). Adicione um método de classe criar_tarefa que receba as informações da tarefa e retorne um objeto Tarefa. Adicione um método que permita alterar o status da tarefa.

class Tarefa:

    tarefas = []
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.status = False
        Tarefa.tarefas.append(self)

    @classmethod
    def criar_tarefa(cls,titulo,descricao):
        return cls(titulo,descricao)
    
    @property
    def status_mudar(self):
        return '✔' if self.status else '✘'


    def alterar_status(self):
         self.status = not self.status

tarefa_1 = Tarefa.criar_tarefa('Jogar lixo', 'Jogar o lixo na lixeira')
tarefa_1.alterar_status()
tarefa_2 = Tarefa.criar_tarefa('Meditar', 'Setar para meditar')
tarefa_3 = Tarefa.criar_tarefa('Treinar', 'Ir para academia')

print(f'Tarefa: {tarefa_1.titulo}\nDescrição: {tarefa_1.descricao}\nStatus: {tarefa_1.status_mudar}')

# 13. Sistema de Vendas
# Crie uma classe Venda com atributos cliente, produtos (uma lista de produtos vendidos) e valor_total. Adicione um método de classe registrar_venda que receba o nome do cliente e uma lista de produtos (com preço) e calcule o valor total. Implemente uma propriedade que retorne a descrição da venda.

class Venda:

    vendas = []
    
    def __init__(self, cliente, produtos, valor_total):
        self.cliente = cliente
        self.produtos = produtos
        self.valor_total = valor_total
        Venda.vendas.append(self)
    
    @classmethod
    def registrar_vendas(cls, cliente, produtos):
        valor_total = sum(produtos.values())
        nova_venda = cls(cliente, produtos, valor_total)
        return nova_venda
    
    @property
    def descricao(self):
        formatacao = '\n'.join([f'{produto}: R$ {preco:.2f}' for produto, preco in self.produtos.items()])
        return (f'\nNome: {self.cliente}\n'
                f'Produtos:\n{formatacao}\n'
                f'Valor Total: R$ {self.valor_total:.2f}\n\n')
    
    @classmethod
    def mostrar_tudo(cls):
        if not cls.vendas:
            return 'Não possui vendas!'
        return '\n'.join([venda.descricao for venda in cls.vendas])


produtos_1 = {'Pá de lixo': 5.99, 'Vassoura': 12.50, 'Jogo americano': 3.00}
venda_1 = Venda.registrar_vendas('Adamos', produtos_1)

produto_2 = {'Sacola de compras' : 13.50, 'Arroz integral' : 13.90, 'Paleta bife' : 36.90}
venda_2 = Venda.registrar_vendas('Alesson', produto_2)

print(Venda.mostrar_tudo())

        
# 14. Gestão de Eventos
# Crie uma classe Evento com atributos nome, data e local. Adicione um método de classe criar_evento que receba as informações do evento e retorne um objeto Evento. Implemente uma propriedade que retorne a descrição do evento, incluindo nome, data e local.

class Evento:

    eventos = []
    def __init__(self, nome, data, local):
        self.nome = nome
        self.data = data
        self.local = local
        Evento.eventos.append(self)

    @classmethod
    def criar_evento(cls,nome, data, local):
        return cls(nome, data, local)
    
    @property
    def descricao(self):
        return (f'Nome: {self.nome}\n'
                f'Data: {self.data}\n'
                f'Local: {self.local}\n')
    
    @classmethod
    def mostrar_evento(cls):
        if not cls.eventos:
            return 'Nenhum evento encontrado!'
        resultado = 'Eventos\n' + '='*30 + '\n'
        for evento in cls.eventos:
            resultado += evento.descricao + '-'*30 + '\n'
        return resultado

evento_1 = Evento.criar_evento('HAlloween', '10/11', 'Rua marilia fatimana, 93')
evento_2 = Evento.criar_evento('Rave', '10/11', 'Chacará do andes, 579')

print(Evento.mostrar_evento())

# 15. Sistema de Inventário
# Crie uma classe ItemInventario que tenha atributos nome, quantidade e preco_unitario. Adicione um método de classe adicionar_item que crie um item e o adicione a uma lista de inventário. Implemente uma propriedade que calcule o valor total do item no inventário (quantidade * preco_unitario).

class ItemInventario:

    todos_os_itens_inventario = []
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        ItemInventario.todos_os_itens_inventario.append(self)
        
    
    @classmethod
    def adicionar_item(cls, nome, quantidade, preco_unitario ):
        return cls(nome, quantidade, preco_unitario)
    
    @property
    def valor_total(self):
        return self.quantidade * self.preco_unitario
    
    @classmethod
    def mostrar_tudo(cls):
        if not cls.todos_os_itens_inventario:
            return 'Não existe itens no inventario!'
        
        resultado = 'Itens do inventario\n'+ '=' * 20+'\n'
        for item in cls.todos_os_itens_inventario:
            resultado += (f'Nome: {item.nome}\n'
                          f'Quantidade: {item.quantidade}\n'
                          f'Preço Unitário: R$ {item.preco_unitario:.2f}\n'
                          f'Valor Total: R$ {item.valor_total:.2f}\n\n')
        return resultado
    
item_1 = ItemInventario.adicionar_item('Mesa', 5, 250)
item_2 = ItemInventario.adicionar_item('Cadeira', 10, 75)


print(ItemInventario.mostrar_tudo())

# 16. Gestão de Reservas de Restaurantes
# Crie uma classe Reserva com atributos cliente, data e numero_de_pessoas. Adicione um método de classe fazer_reserva que receba as informações da reserva e retorne um objeto Reserva. Implemente uma propriedade que retorne a descrição da reserva.

class Reserva:

    reservas = []
    def __init__(self, cliente, data, numero_de_pessoas):
        self.cliente = cliente
        self.data = data
        self.numero_de_pessoas = numero_de_pessoas
        Reserva.reservas.append(self)
    
    @classmethod
    def fazer_reserva(cls, cliente, data, numero_de_pessoas):
        cls(cliente, data, numero_de_pessoas)
    
    @property
    def descricao(self):
        return (f'Cliente: {self.cliente}\n'
                f'Data: {self.data}\n'
                f'Numero de pessoas: {self.numero_de_pessoas}\n')
    
    @classmethod
    def mostrar_reservar(cls):
        if not cls.reservas:
            return 'Não á reservas!'
        resultado = 'Reservas\n'+'-'*25+'\n\n'
        for reserva in cls.reservas:
            resultado += reserva.descricao+'-'*25+'\n'
        return resultado

reserva_1 = Reserva.fazer_reserva('Adamos', '10/11/2024', 4)
reserva_2 = Reserva.fazer_reserva('Alesson', '11/11/2024', 8)

print(Reserva.mostrar_reservar())

# 17. Controle de Funcionários de uma Escola
# Crie uma classe Professor com atributos nome, materia e salario. Adicione um método de classe contratar que receba as informações do professor e retorne um objeto Professor. Implemente uma propriedade que calcule o salário anual do professor.

class Professor:

    professores = []
    def __init__(self, nome, materia, salario):
        self.nome = nome
        self.materia = materia
        self.salario = salario
        Professor.professores.append(self)
    
    @classmethod
    def contratar(cls, nome, materia, salario):
        return cls(nome, materia, salario)
    
    @property
    def salario_anual(self):
        return self.salario * 12
    
    @classmethod
    def descricao(cls):
        resultado = 'Funcionarios\n'+'='*25+'\n' 
        for descricao in cls.professores:
            resultado += (f'Nome: {descricao.nome}\n'
                    f'Materia: {descricao.materia}\n'
                    f'Salario: {descricao.salario:.2f}\n'
                    f'Salario anual: {descricao.salario_anual:.2f}'
                    f'\n'+'-'*25+'\n')
        return resultado

professor_1 = Professor.contratar('Jerônimo', 'História', 2800)
professor_2 = Professor.contratar('Rodolfo', 'Fisíca', 2800)

print(Professor.descricao())
        
# 18. Gestão de Alunos
# Crie uma classe Aluno com atributos nome, curso e nota_final. Adicione um método de classe adicionar_aluno que receba as informações do aluno e retorne um objeto Aluno. Implemente uma propriedade que determine se o aluno está aprovado (nota_final maior ou igual a 7).

class Aluno:

    alunos = []
    def __init__(self, nome, curso, nota_final):
        self.nome = nome
        self.curso = curso
        self.nota_final = nota_final
        Aluno.alunos.append(self)
    
    @classmethod
    def adicionar_aluno(cls, nome, curso, nota_final):
        return cls(nome, curso, nota_final)
    
    @property
    def status(self):
        if self.nota_final >= 7:
            return 'Aprovado!'
        else:
            return 'Reprovado!'
    
    @classmethod
    def descricao(cls):
        if not cls.alunos:
            return 'Não possui alunos!'
        resultado = 'Informação dos alunos\n'+'=' * 30+'\n'
        for aluno in cls.alunos:
            resultado += (f'Nome: {aluno.nome}\n'
                    f'Curso: {aluno.curso}\n'
                    f'Nota final: {aluno.nota_final}\n'
                    f'Status: {aluno.status}'
                    f'\n'+'-'*30+'\n')
        return resultado

aluno_1 = Aluno.adicionar_aluno('Adamos', 'Ciência da computação', 10)    
aluno_2 = Aluno.adicionar_aluno('Alesson', 'Sistema de informação', 10)    
aluno_3 = Aluno.adicionar_aluno('Everton', 'Bombeiro', 5)    

print(Aluno.descricao())

# 19. Sistema de Compras Online
# Crie uma classe Compra com atributos cliente, produtos (uma lista de produtos) e valor_total. Adicione um método de classe realizar_compra que receba o nome do cliente e uma lista de produtos e calcule o valor total. Implemente uma propriedade que retorne a descrição da compra.

class Compra:

    compras = []
    def __init__(self, cliente, produtos, valor_total):
        self.cliente = cliente
        self.produtos = produtos
        self.valor_total = valor_total
        Compra.compras.append(self)

    @classmethod
    def realizar_compra(cls,cliente,produtos):
        valor_total = sum(produtos.values())
        compra = cls(cliente, produtos, valor_total)
        return compra
    
    @property
    def descricao(self):
        formatacao = '\n'.join([f'{produto}: R$ {preco:.2f}' for produto, preco in self.produtos.items()])
        return(f'Cliente: {self.cliente}\n'
               f'Produtos: \n{formatacao}\n'
               f'Valor total: {self.valor_total:.2f}'
               f'\n'+'='*25)
    
    @classmethod
    def mostrar_tudo(cls):
        if not cls.compras:
            return 'Não existe compras!'
        return '\n'.join([compra.descricao for compra in cls.compras])

produtos_para_comprar_1 = {'Saco de lixo' : 3.99, 'Talheres' : 29.90}
compra_1 = Compra.realizar_compra('Adamos', produtos_para_comprar_1)

produtos_para_comprar_2 = {'Suculenta' : 3.99, 'Caixa de som para computador' : 29.90}
compra_2 = Compra.realizar_compra('Alesson', produtos_para_comprar_2)

print(Compra.mostrar_tudo())
        
# 20. Controle de Equipamentos de uma Academia
# Crie uma classe Equipamento com atributos nome, tipo e quantidade. Adicione um método de classe adicionar_equipamento que receba as informações do equipamento e retorne um objeto Equipamento. Implemente uma propriedade que retorne a descrição do equipamento.

class Equipamento:

    equipamentos = []
    def __init__(self, nome, tipo, quantidade):
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade
        Equipamento.equipamentos.append(self)
    
    @classmethod
    def adicionar_equipamento(cls, nome, tipo, quantidade):
        return cls(nome, tipo, quantidade)
    
    @property
    def descricao(self):
        return (f'Nome: {self.nome}\n'
                f'Tipo: {self.tipo}\n'
                f'Quantidade: {self.quantidade}\n')
    
    @classmethod
    def exibir(cls):
        if not cls.equipamentos:
            return 'Não há equipamentos!'
        resultado = '\nEquipementos de academia\n'+'='*30+'\n'
        for equipamento in cls.equipamentos:
            resultado += equipamento.descricao+'\n'+'-' * 30+'\n'
        return resultado
    
equipamento_1 = Equipamento.adicionar_equipamento('Esteira', 'Aerobico', 10)
equipamento_2 = Equipamento.adicionar_equipamento('Barra Olímpica', 'Musculação', 5)

print(Equipamento.exibir())

# class Musica:
#     musicas = []

#     def __init__(self,nome,artista,duracao):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao
#         Musica.musicas.append(self)
    
#     def listar_musicas():
#         for musica in Musica.musicas:
#             print(f'Nome da música: {musica.nome}\nNome do artista: {musica.artista}\nDuração da música: {musica.duracao} minutos') 

# Musica('Lacrimosa - Warum so tief?', 'Tilo wolf', 9.11)
# Musica.listar_musicas()
