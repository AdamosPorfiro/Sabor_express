# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10,'abc']
lista_com_quatro_nomes = ['João', 'Maria', 'José', 'Sião']
lista_comano_de_nascimento_e_ano_atual = [1993, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

for numero in lista_de_numeros:
        if type(numero) == int:
            print(f' → {numero}', end=' ')
print('→ terminou!')  

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma = 0
for numero in lista_de_numeros:
    if type(numero) == int:
        if numero % 2 != 0:
            soma += numero
print(f'\nA soma dos número ímpares é: {soma}\n')

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for i in reversed(lista_de_numeros):
        if type(i) == int:
            print(f' → {i}', end=' ')
print('→ Terminou!')

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero_escolhido = int(input('\n\nInforme um número para receber sua tabuada: '))
for i in range(1,11):
    print(f'{i:2} x {numero_escolhido} = {i*numero_escolhido:3}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

somando = 0
try:
    for numero in lista_de_numeros:
        if isinstance(numero,(int,float)): #Verifica se o valor passado é um determinado tipo
            somando += numero
    print(f'\nA soma de todos os valores da lista é: {somando}')
except TypeError:
        print('Erro: Um dos itens na lista não é um número válido para a soma.')

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

media = (8,10,7,6.5,'abc')
calculo = 0
quantidade_de_medas_na_lista = 0

try:
    for i in media:
        if isinstance(i,(int,float)):
                calculo = i + calculo
                quantidade_de_medas_na_lista += 1
    print(f'\nMédia é de: {calculo / quantidade_de_medas_na_lista:.1f}')

except TypeError:
    print('\nError: A lista está vazia, ou possui valores invalidos por favor verifique a lista de medias')
    
        
    