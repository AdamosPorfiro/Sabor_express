# 3.Crie uma nova classe chamada Carro que herda da classe Veiculo.
# 4.No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.

from Veiculo import Veiculo


class Carro(Veiculo):

    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
    
    def Ligar(self):
        pass
    
    def __str__(self):
       return(  f'Marca: {self._marca}\n'
                f'Modelo: {self._modelo}\n'
                f'Cor: {self.cor}')
    


