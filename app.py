'''
Print exibi uma informação na tela para o usuario;
Para executar utilizando windows, abrimos o terminal e escrevemos: python app.py
'''
#print('Hello,World')
import os
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
""") #Podemos fazer uma quebra de linha utlizado aspas triplas, usamos dependendo da situação
#https://fsymbols.com/pt/ - Alteração da fonte

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n') #\n Pula uma linha

opcao_escolhida = int(input('Escolha uma opção: '))
# opcao_escolhida = int(opcao_escolhida) #input = Recebemos informações do usuario (É possivel passar informação'exibir') criamos uma variavel para armazenar a opção escolhida pelo usuario
# print(type(opcao_escolhida)) #type() = Verifica classe da informação passa no parametro

print(f'Você escolheu a opção {opcao_escolhida}') #Podemos exibir uma mensagem e juntar a informação passada pelo usuario em um print usando fstring = interpolação de string, usando 'f' no inicio da informação e '{}' para invocar a variavel ou função a ser exibida.

def finalizar_app():
     os.system('cls') #no windows
#      os.symlink('clear') no mac
     print('Finalizando o app\n')


#se opcao_escolhida for igual a 1{codigos}
if opcao_escolhida == 1:
    print('Cadastrar restaurante')
#se não se
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
#Se não
else:
#     print('Encerrando o programa')
      finalizar_app()
