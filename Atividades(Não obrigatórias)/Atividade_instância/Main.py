# 7- Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
# 8- Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
# 9- Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

from Exercicio_2_pai import Veiculo
from Exercicio_3_carro_filha import Carro
from Exercicio_4_moto_filha import Moto

moto_1 = Moto('Honda', 'XRE 300', 'Casual')
moto_2 = Moto('Yamaha', 'YZF R-3', 'Esportiva')
moto_3 = Moto('Honda', 'CG 160 TITAN', 'Casual')

Carro_1 = Carro('Volkswagen', 'Gol 1.0', 4)
Carro_2 = Carro('Nissan', 'Livinia 1.6', 4)
Carro_3 = Carro('Volkswagen', 'Fusca 1.5', 2)



def main():
    print(Carro_1, Carro_2, Carro_3, sep='\n\n')
    print('\n',moto_1,moto_2,moto_3, sep='\n\n')

if __name__ == '__main__':
    main()