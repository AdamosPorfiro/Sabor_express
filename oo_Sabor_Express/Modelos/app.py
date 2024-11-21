from Restaurante import Restaurante
from Cardapio.Bebida import Bebida
from Cardapio.Prato import Prato
from Cardapio.Sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça', 'Gourmet',)
bebida_suco = Bebida('Suco de melância', 5.0, 'Grande' )
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_sorvete = Sobremesa('Sorvete de Morango', 8.5, 'Melhor sorvete com pedaços de morango', 'Sorvete', 'Médio')
sobremesa_sorvete.aplicar_desconto()
restaurante_praca.adicionar_item_no_cardapio(bebida_suco)
restaurante_praca.adicionar_item_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_item_no_cardapio(sobremesa_sorvete)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()