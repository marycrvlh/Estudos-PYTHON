#---- LAÇO DE REPETIÇÃO FOR ----
# O laço de repetição for é usado para passar sobre uma sequência (como uma lista, dicionário, tupla ou string) ou para executar um bloco de código um número específico de vezes.

n = 6
for i in range(0, n): #range() é uma função que gera uma sequência de números.
    print(i)

print('---')

nome = 'Mariane'
for letra in nome: #passa por cada letra da string 'Mariane'
    print(letra)

print('---')

#---- FOR DENTRO DE LISTAS ----
# as  listas são coleções ordenadas de elementos, e o laço for pode ser usado para passar por cada elemento da lista.

frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas: #passa por cada elemento da lista 'frutas'
    print(fruta)

print('---')

for i in range(len(frutas)): #passa por cada índice da lista 'frutas'. len() é uma função que retorna o número de elementos em uma sequência.
    print(f'Índice {i}: {frutas[i]}') #acessa o elemento da lista usando o índice

print('---')

#---- FOR DENTRO DE DICIONÁRIOS ----
# dicionário é uma coleção de pares chave-valor, onde cada chave é única e está associada a um valor. O laço for pode ser usado para passar sobre as chaves, valores ou ambos em um dicionário.

pessoa = {'nome': 'Mariane', 'idade': 17, 'cidade': 'São Paulo'}
for chave, valor in pessoa.items(): #passa por cada par de chave-valor do dicionário 'pessoa'
    print(f'{chave}: {valor}') 

print('---')

#---- EXEMPLO PRÁTICO: TABUADA ----
num = int(input('Digite um número para ver a tabuada: '))
for i in range(1, 11): #passa por cada número de 1 a 10
    resultado = num * i
    print(f'{num} x {i} = {resultado}')