#---- LAÇO DE REPETIÇÃO WHILE ----
# O laço de repetição while é usado para executar um bloco de código enquanto uma condição for verdadeira. Ele é útil quando não sabemos o número exato de iterações que precisamos.

contador = 0
while contador < 5: #enquanto o contador for menor que 5, o bloco de código será executado
    print(f'Contador: {contador}')
    contador += 1 #incrementa o contador em 1 a cada iteração

print('---')

tentativas = 3
while tentativas > 0: #enquanto houver tentativas restantes, o bloco de código será executado
    print(f'Tentativas restantes: {tentativas}')
    tentativas -= 1 #decrementa as tentativas em 1 a cada iteração

print('---')

#---- EXEMPLO PRÁTICO: SENHA ----
senhaCorreta = '1234'
senhaUsuario = input('Digite a senha: ')
while senhaUsuario != senhaCorreta: #enquanto a senha do usuário for diferente da senha correta, o bloco de código será executado
    print('Senha incorreta. Tente novamente.')
    senhaUsuario = input('Digite a senha: ')
print('Senha correta. Acesso concedido.')