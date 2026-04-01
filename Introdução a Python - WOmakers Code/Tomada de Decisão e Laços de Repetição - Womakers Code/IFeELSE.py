#---- CONDICÇÕES COM IF, ELIF E ELSE ----
# A estrutura condicional if é usada para tomar decisões com base em condições oferecidas pelo usuário. O elif (else if) é usado para verificar múltiplas condições, e o else é usado para lidar com casos que não se encaixam nas condições anteriores.

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você é maior de idade.')
elif idade >= 13:
    print('Você é um adolescente.')
else:
    print('Você é uma criança.')

#---- EXEMPLO PRÁTICO: RECUPERAÇÃO OU APROVAÇÃO ----
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print('Você foi aprovado!')
elif media >= 5:
    print('Você está de recuperação.')
else:
    print('Você foi reprovado.')
