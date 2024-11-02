# 1.Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

class ContaBancaria:

    contas = []
    def __init__(self,titular,saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)
# 2.Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    
    def __str__(self):
        return f'Olá, Sr. {self._titular}!\nO saldo: R$ {self._saldo:.2f}\nSua conta está: {'Ativa' if self._ativo else 'Desativada'}'

# 3.Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    
    @classmethod
    def alterar_estado(cls,conta):
        conta._ativo = True
        

pessoa_1 = ContaBancaria('Adamos',500)
pessoa_2 = ContaBancaria('Everton',776)

ContaBancaria.alterar_estado(pessoa_1)
print(f'{pessoa_1}\n\n{pessoa_2}')
# 4.Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

class ContaBancaria:

    contas = []
    def __init__(self,titular,saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    @property
    def descricao(self):
        return (f'\nTitular: {self._titular}\n'
                f'Saldo: R$ {self._saldo:.2f}\n'
                f'Status da conta: {'Ativa' if self._ativo else 'Desativado'}\n')
    @classmethod
    def dados_das_contas(cls):
        if not cls.contas:
            return 'Não existe contas!'
        return f'\n'.join([dados.descricao for dados in cls.contas])
    
    @property 
    def titular(self):
        return self._titular
    
pessoa_1 = ContaBancaria('Adamos',500)
ContaBancaria.alterar_estado(pessoa_1)
pessoa_2 = ContaBancaria('Everton',776)

# 5.Crie uma instância da classe e imprima o valor da propriedade titular.

class ContaBancaria:

    contas = []
    def __init__(self,titular,saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)
    
    def alterar_estado(self):
        self._ativo = not self._ativo
    
    @property 
    def titular(self):
        return self._titular

pessoa_3 = ContaBancaria('Alesson', 10.000)
print(f'\nTitular: {pessoa_3.titular}\n')

# 6.Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

class ClienteBanco:

    def __init__(self, nome, saldo, sacar, depositar,numero_conta):
        self._nome = nome
        self._saldo = saldo
        self._ativo = False
        self.sacar = sacar
        self.depositar = depositar
        self.numero_conta = numero_conta

    def __str__(self):
        return (f'Nome: {self._nome}\n'
                f'Saldo: {self._saldo:.3f}\n'
                f'Status: {'Ativo' if self._ativo else 'Desativado'}')

    def alterar_status(self):
        self._ativo = not self._ativo

cliente_1 = ClienteBanco('Adamos', 1.500, None, None, None)
cliente_1.alterar_status()
print(cliente_1)

# 7.Crie um método de classe para a conta ClienteBanco.

class ClienteBanco:

    clientes = []
    def __init__(self, nome, saldo, sacar, depositar, numero_conta):
        self._nome = nome
        self._saldo = saldo
        self._ativo = False
        self.sacar = sacar
        self.depositar = depositar
        self.numero_conta = numero_conta
        ClienteBanco.clientes.append(self)

    @classmethod
    def descricao(cls):
        if not cls.clientes:
            return 'Não existe clientes!'
        resultado = ''
        for dados in cls.clientes:
            resultado += (f'\nNome: {dados._nome}\n'
                          f'Saldo: {dados._saldo:.2f}\n'
                          f'Status: {'Ativo' if dados._ativo else 'Desativado\n'}')
        return resultado

    def alterar_status(self):
        self._ativo = not self._ativo

cliente_1 = ClienteBanco('Hamilton', 1500, None, None, None)
cliente_1.alterar_status()

print(ClienteBanco.descricao())