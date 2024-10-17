# Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:

    def __init__(self,nome,idade,profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nProfissão: {self.profissao}'
    
    @classmethod
    def aniversario(cls, incremento):
        incremento.idade += 1
    
    @property
    def saudacao(self):
        return f'Caro Sr. {self.nome} seja bem vindo a profissão de {self.profissao}!'

pessoa_1 = Pessoa('Adamos', 30, 'Porteiro')
Pessoa.aniversario(pessoa_1)
print(pessoa_1)
print(pessoa_1.saudacao)
