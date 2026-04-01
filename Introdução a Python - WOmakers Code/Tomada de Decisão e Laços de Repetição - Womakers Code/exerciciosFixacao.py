# Exercício 1 Crie uma variável com a quantidade de aulas concluídas. Se for maior ou igual a 5, exiba "Bom progresso!". Caso contrário, exiba "Continue estudando".
aulasConcluidas = int(input('Digite a quantidade de aulas concluídas: '))
if aulasConcluidas >= 5:
    print('Bom progresso!')
else:
    print('Continue estudando.')

# Exercício 2 Crie um programa que exiba os números de 1 a 10 usando while.
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# Exercício 3 Use for para exibir os números de 1 a 5 acompanhados da mensagem: "Aula concluída". 
for i in range(1, 6):
    print(f'{i} - Aula concluída')


# Exercício 4 Crie uma lista com os dias da semana que você pretende estudar. Use for para exibir cada dia.
diasSemana = ['Segunda-feira', 'Quarta-feira', 'Sexta-feira']
for dia in diasSemana:
    print(dia)


# Exercício 5 Crie uma variável com a idade de uma pessoa. Use if else para verificar se ela pode se inscrever em um curso que exige idade mínima de 16 anos.
idade = int(input('Digite a sua idade: '))
if idade >= 16:
    print('Você pode se inscrever no curso.')
else:
    print('Você não pode se inscrever no curso.')