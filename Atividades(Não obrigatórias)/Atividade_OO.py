# 1.Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

restaurantes = [restaurante_praca]

print(vars(restaurantes[0]))

# 2.Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

print(f'Categoria: {restaurantes[0].categoria}')

# 3.Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

if restaurantes[0].ativo == False:
    print('Restaurante Praça está INATIVO!')
else:
    print('Restaurante Praça está ATIVO!')
    
# 4.Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
# 5.Altere o valor do atributo nome para 'Bistrô'.
# 6.Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
# 7.Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
# 8.Mude o estado da instância restaurante_pizza para ativo.
# 9.Imprima no console o nome e a categoria da instância restaurante_praca.