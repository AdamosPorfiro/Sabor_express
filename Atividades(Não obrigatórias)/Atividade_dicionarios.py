# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

dados_pessoais = {
    'nome':'Adamos', 'idade':30, 'cidade':'Barueri'
    }


# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
dados_pessoais['idade'] = 35
print(dados_pessoais)
#ou
dados_pessoais.update({'idade':30})
print(dados_pessoais)

# Adicione um campo de profissão para essa pessoa;
dados_pessoais['profissao'] = 'Porteiro'
print(dados_pessoais)
# ou
dados_pessoais.update({'profissao':'Seguranca'})
print(dados_pessoais)

# Remova um item do dicionário.
dados_pessoais.pop('profissao')
print(dados_pessoais)

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
numeros_em_drobro = (
    {1:1*1, 2:2*2, 3:3*3, 4:4*4, 5:5*5}
)
print(numeros_em_drobro)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

verificacao_de_dados = dados_pessoais.get('profissao', 'Não existe dados da profissao do usuario!')
print(verificacao_de_dados)

    # 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frequencia = {}
from os import system

def contandor():
    system('cls')
    palavras = input('Digite uma frase: ').split()

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1   

def resposta():
    resp = input('\nDeseja continuar[S/N]: ').upper().strip()
    if resp == 'S':
        menu_principal()
    else:
        finalizando_programa()

def finalizando_programa():
    print('\n')
    for palavra in frequencia:
        print(f'Você escreveu {palavra}: {frequencia.get(palavra, 'Valor não existe')} vezes')
    print('\nFinalizando o programa!')
    

def menu_principal():
    contandor()
    resposta()

if __name__ == '__main__':
    menu_principal()

