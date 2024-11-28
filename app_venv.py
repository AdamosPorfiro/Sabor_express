"""
Aqui temos um arquivo que vai acessar um .json que possui uma quantidade de dados, informações referentes a restaurantes e o cardapio,
vamos importar a biblioteca request que vai permitir que possamos acessar esses arquivos de forma que, tenhamos Requisições e Respostas 
"""

import requests #Biblioteca de requisições e respostas
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' #Esse arquivo é muito comumente usado em programação, chamad JSON

"""
Essa variavel acessa a variavel url que é onde o nosso arquivo .json está, utilizando uma função da biblioteca .get 
response = resposta que teremos
"""
response = requests.get(url)

'''
Se o acesso ao arquivo for um sucesso e a resposta corresponder, geralmente gera o código 200 e o nosso arquivo .json é transformado em um dicionario python
através da variavel dados_json. Temos um dicionarios vazio e vamos interar com for para acessar esses dados. Para cada item dentro do dicionario vamos acessar o item com nome Company, feito isso temos uma condição que vai verificar se o nome passado realmente existe dentro do nosso arquivo Json, Se não existir teremos uma variável que irá criar uma lista vazia e armazenar a interação que for encontrada, quando ele encontra ele armazena as informações descritas (Item, Price, Description), caso contrário ele mostra o código do erro.

Quando printamos é passado a chave que será o nome do restaurante, deve ser exatamente igual está no arquivo .Json
'''
if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append ({
            'item' : item['Item'],
            'price' : item['price'],
            'description' : item['description']
        })


else:
    print(f'O erro foi {response.status_code}')

'''
Essa interação cria arquivos json separando e filtrando o arquivo com base nos nomes dos restaurantes
'''

for nome_do_restaurante, dados in dados_restaurante.items():
    '''
    Temos a chave que será o nome do restaurante e valores que são os dados, 1° variável é o nome do nosso arquivo, with open permite manipular os arquivos também dentro da aplicação, passamos 2 informações que é o nome do nosso arquivo e w = write(escrever) e vamos nomear  o nome desse arquivo com o nome arquivo_restaurante usamos 'as'

    Para criar o aquivo importamos a biblioteca .json e usamos a função dump que vai converter o dicionário em um arquivo string, passamos 3 informações, o valor de for (dados) | arquivo_restaurante que estamos trabalhando e por último a identação para ficar mais legível 
    '''
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
