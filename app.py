'''
Print exibi uma informação na tela para o usuario;
Para executar utilizando windows, abrimos o terminal e escrevemos: python app.py
'''
#print('Hello,World')
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

opcao_escolhida = input('Escolha uma opção: ')#input = Recebemos informações do usuario (É possivel passar informação'exibir') criamos uma variavel para armazenar a opção escolhida pelo usuario
print(f'Você escolheu a opção {opcao_escolhida}') #Podemos exibir uma mensagem e juntar a informação passada pelo usuario em um print usando fstring = interpolação de string, usando 'f' no inicio da informação e '{}' para invocar a variavel ou função a ser exibida.


