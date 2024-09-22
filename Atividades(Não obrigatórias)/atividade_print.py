"""1 - Imprima a frase: Python na Escola de Programação da Alura.

2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

A
L
U
R
A

4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:

pi = 3.14159
"""
from math import ceil, floor #Importação de 2 modulos da biblioteca math, também podemos importar tudo usando: import math

print('Python na Escola de Programação da Alura\n')
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
print(f'Meu nome é {nome} e tenho {idade} anos')
print('''
A
L
U
R
A
''')
pi = 3.14159 #Função round arredonda o número para o mais próximo Ex: 3.14159 = 3 ou 3.85678 = 4 podemos também definir quantas casa decimais indicando como paramêtro a quantidade de casas
print(f'''
Arredondamento com dois decimais {round(pi,2)}.
Arredondamento para cima: {ceil(pi)}.
Arredondamento para baixo {floor(pi)}.
''') #Ceil = Arredonda para cima + | floor = Arredonda para baixo -