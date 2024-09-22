"""1 - Imprima a frase: Python na Escola de Programação da Alura.

2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

A
L
U
R
A"""

print('Python na Escola de Programação da Alura\n')
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
print(f'Meu nome é {nome} e tenho {idade} anos')
print("""
A
L
U
R
A""")