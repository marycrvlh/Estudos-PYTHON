#Menu de opções utilizando laço de repetição while

#variaveis de controle
contador = 0
opcao = 0

#exibindo o menu de opções e solicitando a escolha do usuário
while True:
    print('Menu de opções:')
    print('1 - Mensagem')
    print('2 - Contador')
    print('3 - Sair')
    opcao = int(input('Digite a opção desejada: '))

#mostrando o resultado da escolha do usuário
    if opcao == 1:
        print('Olá, seja bem-vinda ao mundo da programação!') #mensagem de boas-vindas
    elif opcao == 2:
        contador += 1
        print(f'Contador: {contador}') #mostrando quantas vezes o menu foi acessado
    elif opcao == 3:
        print('Saindo do programa. Até mais!') #mensagem de despedida
        break
    else:
        print('Opção inválida. Tente novamente.') #tratamento de erro para opções inválidas