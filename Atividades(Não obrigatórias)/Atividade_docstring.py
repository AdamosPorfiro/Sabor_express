# Crie uma docstring para a função exibir_nome_do_programa()
'''
Essa função exibe o nome do programa.

Output
- Print - Que exibe o nome do programa para o usuario.
'''

# Crie uma docstring para a função exibir_opcoes()
'''
Essa função exibe as opções para navegar no aplicativo.

Output:
- Print - Opções para o usuario escolher.
'''

# Crie uma docstring para a função finalizar_app()
'''
Essa função exibe para o usuario o texto de finalização, fechamento do aplicativo.

Output:
- Print - exibe um texto finalizando o aplicativo.
'''

# Crie uma docstring para a função opcao_invalida()
'''
Essa função é responsavel por exibir para o usuario, que a opção escolhida é invalida e retorna ao menu principal.

Input:
- input - Perguntando se quer escolher outra opção ou voltar ao menu principal.

Output:
- Print - exibindo que a opção escolhida é invalida.
'''

# Crie uma docstring para a função exibir_subtitulo(texto)
'''
Essa função é responsavel por exibir os textos, subtitulos do aplicativo.

Input:
- Parametro(texto) - Quando invocarmos essa função, o parametro passado na função receberá uma entrada.

Output:
- Print - Exibir o parâmetro passado.
'''

# Crie uma docstring para a função cadastrar_novo_restaurante()
'''
Essa função é responsavel por cadastrar um novo restaurante.

- While - Vai repetir um novo cadastro em quanto a resposta do usuario for S (SIM);

Input:
- Nome do restaurante;
- Categoria do restaurante;
- Se o cliente deseja continuar cadastrando restaurantes.

Output:
- Dados do restaurante;
- Esses dados serão enviados para a lista de restaurantes;
- Exibe informaçao de cadastro para o cliente;
- Se resposta for S(SIM) o While repete novamente os input's e outpu'ts.
'''

# Crie uma docstring para a função listar_restaurantes()
'''
Essa função é responsavel por listar os restaurantes cadastrados para os usuarios.

Input:
- Print exibe a lista de restaurantes;
- For que exibe item cadastrado do restaurante separadamente;
- Retorna ao menu principal.
'''

# Crie uma docstring para a função alternar_estado_restaurante()
'''
Essa função permite alterar o estado de um restaurante cadastrado para ativado ou desativado

Essa função permite alterar o estado de um restaurante cadastrado para ativado ou desativado

Input:
- Nome do restaurante que deseja alterar;
- Variavel restaurante_encontrado inicializada como False;
- Vamos iterar com for e verificar se o restaurante existe, caso sim ele ativa o restaurante ou desativa;

Output:
- Print que exibe para o usuario se o restaurante foi ativado ou não;
- Caso não exista o nome passado como input, ele exibe que não foi encontrado;
- Por fim ele retorna ao menu principal.

'''

# Crie uma docstring para a função escolher_opcao()
'''
    Essa função permite o usuario acessar as demais funções do aplicativo que são exibidas da função exibir_opcoes

Input:
- Usuario deve escolher uma das opções exibidas pela função exibir_opcoes();

Output:
- Caso a opção seja valida o usuario será redirecionado para a tela escolhida;
- Por fim caso a opção não exista ele irá invocar função opção_invalida().

Temo um Try except para lidar com possiveis erros.
'''

# Crie uma docstring para a função main()
'''
Essa função faz a limpeza do menu e exibe em seguida todo o menu de opções para o usuario navegar no aplicativo

Input:
- Invocamos a função de escolher_opções permitindo que o usuario itere com o aplicativo

Output:
- Faz a limpeza da tela utilizando biblioteca 'os' modulo 'cls';
- Invocamos a função exibir nome do programa();
- Invocamos a função exibir as opções para o usuario visualisar e navegar pelo aplicativo;
'''