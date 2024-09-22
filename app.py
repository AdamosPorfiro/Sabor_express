'''
Print exibi uma informação na tela para o usuario;
Para executar utilizando windows, abrimos o terminal e escrevemos: python app.py
'''
#print('Hello,World')
from os import system
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

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida) #input = Recebemos informações do usuario (É possivel passar informação'exibir') criamos uma variavel para armazenar a opção escolhida pelo usuario
    # print(type(opcao_escolhida)) #type() = Verifica classe da informação passa no parametro
    
    print(f'Você escolheu a opção {opcao_escolhida}') #Podemos exibir uma mensagem e juntar a informação passada pelo usuario em um print usando fstring = interpolação de string, usando 'f' no inicio da informação e '{}' para invocar a variavel ou função a ser exibida.
    #se opcao_escolhida for igual a 1{codigos}
    match opcao_escolhida:
        case 1:
            print('Cadastrar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            finalizar_app()
        case _:
            print('Opção inválida')
          
    """if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    #se não se
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    #Se não
    else:
    #     print('Encerrando o programa')
        finalizar_app()"""

def finalizar_app(): # def = Definição, cria uma função
     system('cls') #no windows
#    system('clear') no mac
     print('Finalizando o app\n')

def main():
     exibir_nome_do_programa()
     exibir_opcoes()
     escolher_opcao()

if __name__ == '__main__':
     main()

