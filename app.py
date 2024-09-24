'''
Print exibi uma informação na tela para o usuario;
Para executar utilizando windows, abrimos o terminal e escrevemos: python app.py
'''
#print('Hello,World')
from os import system
restaurantes = [] # Lista = Usamos colchetes, para criar uma lista

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
    ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)
    #Podemos fazer uma quebra de linha utlizado aspas triplas, usamos dependendo da situação
    #https://fsymbols.com/pt/ - Alteração da fonte

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n') #\n Pula uma linha

def cadastrar_novo_restaurante():
    system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante) #.append = Adiciona na lista a informação
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('Aperte enter para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def escolher_opcao():
    try: # Permite que você teste um bloco de código em busca de erros, se houver algum erro ele vai executar o except, se não houver erro ele segue o bloco de código naturalmente
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida) #input = Recebemos informações do usuario (É possivel passar informação'exibir') criamos uma variavel para armazenar a opção escolhida pelo usuario
        # print(type(opcao_escolhida)) #type() = Verifica classe da informação passa no parametro
        
        print(f'Você escolheu a opção {opcao_escolhida}') #Podemos exibir uma mensagem e juntar a informação passada pelo usuario em um print usando fstring = interpolação de string, usando 'f' no inicio da informação e '{}' para invocar a variavel ou função a ser exibida.
        #se opcao_escolhida for igual a 1{codigos}
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except: # Permite que você lide com o erro 
        opcao_invalida()
        
    """if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    #se não se
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    #Se não
    elif:
    #   print('Encerrando o programa')
        finalizar_app()
    else:
        opcao_invalida()"""

def finalizar_app(): # def = Definição, cria uma função
     system('cls') #no windows
#    system('clear') no mac
     print('Finalizando o app\n')

def main():
     system('cls')
     exibir_nome_do_programa()
     exibir_opcoes()
     escolher_opcao()

if __name__ == '__main__':
     main()

