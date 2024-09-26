# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_com_quatro_nomes = ['João', 'Maria', 'José', 'Sião']
lista_comano_de_nascimento_e_ano_atual = [1993, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# for numero in lista_de_numeros:
#     if  type(numero) == int:
#         print(f' → {numero}', end=' ')
#     else:
#         print(' → Terminou')    

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
# soma = 0
# for numero in lista_de_numeros:
#     if numero % 2 != 0:
#         soma += numero
# print(f'A soma dos número ímpares é: {soma}')

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in reversed(lista_de_numeros):
    if type(i) == int:
        print(f' → {i}', end=' ')

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.