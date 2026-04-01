#Exercício 1
#Crie variáveis para armazenar:
#● Seu nome
#● Sua área de interesse em tecnologia
#● Quantas horas por semana você pretende estudar
#Depois, exiba essas informações em uma mensagem completa.

nome = input('Qual é o seu nome? ')
area_interesse = input('Qual é a sua área de interesse em tecnologia? ')
horas_estudo = int(input('Quantas horas por semana você pretende estudar? '))

print(f'Olá, {nome}! Você está disposto a estudar {horas_estudo} horas por semana para entrar na área de {area_interesse}.')

#Exercício 2
#Crie duas variáveis com números inteiros representando:
#● Número de aulas assistidas
#● Número total de aulas do curso
#Calcule e exiba quantas aulas ainda faltam.
aulas_assistidas = int(input('Quantas aulas você já assistiu? '))
total_aulas = int(input('Quantas aulas tem o curso? '))
aulas_faltantes = total_aulas - aulas_assistidas
print(f'Você ainda tem {aulas_faltantes} aulas para assistir.')

#Exercício 3
#Crie uma variável com um valor decimal representando o tempo de estudo diário em horas. Exiba esse valor na tela.
tempo_estudo_diario = float(input('Quantas horas por dia você estuda? '))
print(f'Você estuda {tempo_estudo_diario} horas por dia.')

#Exercício 4
#Use o operador % (resto) para verificar se o número de horas totais de estudo na semana é par ou ímpar.
horas_semana = tempo_estudo_diario * 7 #são os dias que tem em uma semana
if horas_semana % 2 == 0:
    print(f'O número de horas totais de estudo na semana é par.')
else:
    print(f'O número de horas totais de estudo na semana é ímpar.')

#Exercício 5
#Crie uma variável com o número de semanas de estudo e use += para simular o avanço de mais uma semana.
semanas_estudo = int(input('Quantas semanas de estudo você já completou? '))
semanas_estudo += 1
print(f'Após mais uma semana de estudo, você terá estudado por {semanas_estudo} semanas.')