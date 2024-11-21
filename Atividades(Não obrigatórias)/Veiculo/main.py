# 5.Em um arquivo chamado main.py, importe a classe Carro.
# 6.No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.

from Carro import Carro

carro_1 = Carro('Volkswagen', 'Gol 1.0', 'Cinza')
carro_2 = Carro('Nissan', 'Livinia 1.6', 'Verde')
carro_3 = Carro('Honda ', 'HRV  1.5', 'Branca')



def main():
    print(f'{carro_1}\n\n{carro_2}\n\n{carro_3}')

if __name__ == '__main__':
    main()