from Restaurante import Restaurante
from Cardapio.Bebida import Bebida
from Cardapio.Prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet',)
bebida_suco = Bebida('Suco de melância', 5.0, 'Grande' )
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')



def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()