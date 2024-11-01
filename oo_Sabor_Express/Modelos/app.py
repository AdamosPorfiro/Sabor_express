from Restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet',)
restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
restaurante_mexicano.alternar_estado()
restaurante_japones = Restaurante('Japa', 'Japonesa')


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()