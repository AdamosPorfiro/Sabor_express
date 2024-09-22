'''1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

from os import system
def impar_ou_par():
    system('cls')
    numero = int(input('Informe um número para verificar se é ímpar ou par\n'))
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
impar_ou_par()
'''
'''
2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.

from os import system
def categoria_idade():
    system('cls')
    idade = int(input('Qual a sua idade: '))

    if idade <= 12:
        print(f'Você tem {idade} anos. Sua categoria é CRIANÇA')
    elif 13 <= idade <= 18:
        print(f'Você tem {idade} anos. Sua categoria é ADOLESCENTE')
    else:
        print(f'Você tem {idade} anos. Sua categoria é ADULTO')
categoria_idade()    
'''

'''
3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

from os import system
def acessando_conta():
    system('cls')
    nome_usuario = 'Adamos'
    senha_usuario = 'Adamos1993'

    usuario = input('Usuario: ')
    senha = input('Senha: ')

    if nome_usuario == usuario and senha_usuario == senha:
        print('Login efetuado com sucesso!')
    else:
        print('Login ou senha inválidos! Tente novamente')

acessando_conta()
'''

'''
4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.'''

from os import system
def quadrante_cartesiano():
    system('cls')
    x = int(input('Informe valor de x: '))
    y = int(input('Informe valor de y: '))

    if x > 0 and y > 0:
        print('Primeiro quadrante')
    elif x < 0 and y > 0:
        print('Segundo quadrante')
    elif x < 0 and y < 0:
        print('Terceiro quadrante')
    elif x > 0 and y < 0:
        print('Quarto quadrante')
    else:
        print('O ponto está no eixo ou origem')

quadrante_cartesiano()