
#---- TIPOS DE DADOS ----
# números ineteiros: int() (faz a conversão de um valor)
num1 = 10
num2 = 5
print(num1, num2)
produto = int(float(input('Digite o valor do produto: '))) #faz a conversão de um valor string para float e depois para int
print(f'O valor do produto será de: {produto}')

# números decimais: float() (faz a conversão de um valor) + round() para arredondar o valor
num3 = 3.14
print(num3) #valor decimal normal (3.14)
print(round(num3)) #valor arredondado (3)

# texto ou caractere: str() + slice() para fatiar o texto
texto = 'Olá, mundo!'
print(texto) #texto completo
print(texto[0]) #navegou até a posição 1 do texto (letra 'O')
print(texto[0:3]) #navegou do início até a posição 3 (letras 'Olá')

# ---- OPERAÇÕES MATEMÁTICAS ----
num1 = 10
num2 = 5

# soma: +
soma = num1 + num2
print(f'A soma de {num1} e {num2} é: {soma}')

# subtração: -
subtracao = num1 - num2
print(f'A subtração de {num1} e {num2} é: {subtracao}')

# multiplicação: *
multiplicacao = num1 * num2
print(f'A multiplicação de {num1} e {num2} é: {multiplicacao}')

# divisão: /
divisao = num1 / num2
print(f'A divisão de {num1} e {num2} é: {divisao}')

# divisão inteira: //
divisao_inteira = num1 // num2
print(f'A divisão inteira de {num1} e {num2} é: {divisao_inteira}')

# módulo: % (resto da divisão)
modulo = num1 % num2
print(f'O módulo de {num1} e {num2} é: {modulo}')

# exponenciação: **
exponenciacao = num1 ** num2 #10 elevado a 5
print(f'A exponenciação de {num1} e {num2} é: {exponenciacao}')

#---- OPERAÇÕES ESPECIAIS ----

# incremento: += (adiciona um valor a uma variável)
num1 += 5 #10 + 5 = 15
print(f'O valor de num1 após o incremento é: {num1}')

# decremento: -= (subtrai um valor de uma variável)
num1 -= 3 #15 - 3 = 12
print(f'O valor de num1 após o decremento é: {num1}')

#---- OPERADORES RELACIONAIS E PRECEDÊNCIA ----

# operadores relacionais (comparação): ==, !=, >, <, >=, <=
print(num1 == num2) #verifica se num1 é igual a num2 (False)
print(num1 != num2) #verifica se num1 é diferente de num2 (True)
print(num1 > num2) #verifica se num1 é maior que num2 (True)
print(num1 < num2) #verifica se num1 é menor que num2 (False)
print(num1 >= num2) #verifica se num1 é maior ou igual a num2 (True)
print(num1 <= num2) #verifica se num1 é menor ou igual a num2 (False)

# operadores de precedência (prioridade): (), **, *, /, +, -
resultado = (num1 + num2) * 2 #a soma é feita primeiro, depois a multiplicação 
print(f'O resultado da expressão é: {resultado}')