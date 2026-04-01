#Fase 1: Coleta de Dados
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura em metros: '))
anoAtual = int(input('Digite o ano atual: '))

#Fase 2: Interação Personalizada
print(f'Olá, {nome}! Seja Bem-Vinda ao mundo da programação!')

#Fase 3: Cálculos

#Linha do tempo
anoNascimento = anoAtual - idade
print(f'Você nasceu em {anoNascimento} e tem {idade} anos. Em 5 anos, você terá {idade + 5} anos.')

#Operação Especial
idadeDobro = idade * 2
idadeElevada = idade ** 2
print(f'Idade dobrada: {idadeDobro}')
print(f'Idade elevada ao quadrado: {idadeElevada}')

#Fase 4: Lógica e Comparações
if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

if altura >= 1.60:
    print('Você tem altura minima.')
else:
    print('Você não tem altura minima.')
