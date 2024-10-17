# 1.Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

class ContaBancaria:

    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

# 2.Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    
    def __str__(self):
        return f'Olá, Sr. {self.titular}!\nO saldo: R$ {self.saldo:.2f}.'

# 3.Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    
    def alterar_estado(self):
        self._ativo = not self._ativo

pessoa_1 = ContaBancaria('Adamos Porfiro',500)
pessoa_2 = ContaBancaria('Everton delmondes',776)

ContaBancaria.alterar_estado(pessoa_1)
print(pessoa_1)
# 4.Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.



# 5.Crie uma instância da classe e imprima o valor da propriedade titular.

# 6.Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

# 7.Crie um método de classe para a conta ClienteBanco.