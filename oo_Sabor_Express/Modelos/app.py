from Restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet',)
# restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
# restaurante_mexicano.alternar_estado()
# restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Laís', 8)
restaurante_praca.receber_avaliacao('Emy', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()