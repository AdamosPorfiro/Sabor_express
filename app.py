'''
Print exibi uma informação na tela para o usuario;
Para executar utilizando windows, abrimos o terminal e escrevemos: python app.py
'''
#print('Hello,World')
from os import system
# restaurantes = ['Pizza', 'Sushi'] # Lista = Usamos colchetes, para criar uma lista
# #                  0       1
# #                ativo   desativado
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza suprema', 'categoria':'Italiana','ativo':True},
                {'nome':'Cantina','categoria':'Italiano','ativo':False}
]

def exibir_nome_do_programa():
    print("""
            ░██████╗░█████╗░██████╗░░█████╗░██████╗░
            ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
            ╚█████╗░███████║██████╦╝██║░░██║██████╔╝
            ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
            ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
            ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝
    ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")
    #Podemos fazer uma quebra de linha utlizado aspas triplas, usamos dependendo da situação
    #https://fsymbols.com/pt/ - Alteração da fonte

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n') #\n Pula uma linha
    
def cadastrar_novo_restaurante():
    resp = 'S'
    while resp == 'S':
        exibir_textos('Cadastro de novos restaurantes')
        nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
        categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
        dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
        restaurantes.append(dados_do_restaurante)
        exibir_textos(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

        resp = input('Deseja cadastrar mais restaurantes [S/N]: ').upper().strip()
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    exibir_textos(input('\nAperte "ENTER" para voltar ao menu principal '))
    main()

def opcao_invalida():
    exibir_textos('Opção inválida!')
    voltar_ao_menu_principal()

def exibir_textos(texto):
    system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def listar_restaurantes():
    exibir_textos('Lista de restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    print('-' * 60)
    for i in restaurantes: #Para cada restaurante na lista restaurante print
        nome_restaurate = i['nome']
        categoria = i['categoria']
        ativo = 'ativado' if i['ativo'] else 'desativado' # Ternario
        print(f'- {nome_restaurate.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def escolher_opcao():
    try: # Permite que você teste um bloco de código em busca de erros, se houver algum erro ele vai executar o except, se não houver erro ele segue o bloco de código naturalmente
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida) #input = Recebemos informações do usuario (É possivel passar informação'exibir') criamos uma variavel para armazenar a opção escolhida pelo usuario
        # print(type(opcao_escolhida)) #type() = Verifica classe da informação passa no parametro
        # exibir_textos(f'Você escolheu a opção {opcao_escolhida}') #Podemos exibir uma mensagem e juntar a informação passada pelo usuario em um print usando fstring = interpolação de string, usando 'f' no inicio da informação e '{}' para invocar a variavel ou função a ser exibida.
        #se opcao_escolhida for igual a 1{codigos}
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante() 
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except: # Permite que você lide com o erro 
        opcao_invalida()
        
    # if opcao_escolhida == 1:
    #     print('Cadastrar restaurante')
    # #se não se
    # elif opcao_escolhida == 2:
    #     print('Listar restaurantes')
    # elif opcao_escolhida == 3:
    #     print('Ativar restaurante')
    # #Se não
    # elif:
    # #   print('Encerrando o programa')
    #     finalizar_app()
    # else:
    #     opcao_invalida()

def alternar_estado_restaurante():
    exibir_textos('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O resurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O  {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
    voltar_ao_menu_principal()

def finalizar_app(): # def = Definição, cria uma função
     exibir_textos('Finalizando o app')
#    system('cls') #no windows
#    system('clear') no mac

def main():
     system('cls')
     exibir_nome_do_programa()
     exibir_opcoes()
     escolher_opcao()

if __name__ == '__main__':
     main()

