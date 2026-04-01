#--- DICIONARIOS EM PYTHON ---
#os dicionários são estruturas de dados que armazenam pares de chave-valor. Eles são mutáveis, ou seja, os dados dentro de um dicionário podem ser alterados depois de criados. Eles são representados por chaves {} e os pares de chave-valor são separados por vírgula. A chave é usada para acessar o valor correspondente.

cadastro = {'nome': 'Mari',
            'idade': 17,
            'cidade': 'São Paulo',
            'profissão': 'estudante'}
print(cadastro) #mostra o dicionário completo
print(cadastro['nome']) #mostra o valor correspondente à chave 'nome' (Mari)

cadastro['profissão'] = 'programadora' #altera o valor correspondente à chave 'profissão' para 'programadora'
print(cadastro) #mostra o dicionário atualizado

cadastro.pop('cidade') #remove o par de chave-valor correspondente à chave 'cidade'
print(cadastro) #mostra o dicionário atualizado


#Mosclando dicionários em uma lista
faculdade = [
              {'nome': 'Maria', 'curso': 'Ciência da Computação'},
              {'nome': 'João', 'curso': 'Engenharia de Software'},
              {'nome': 'Ana', 'curso': 'Sistemas de Informação'}]

for aluno in faculdade:
    print(f'nome: {aluno["nome"]}, curso: {aluno["curso"]}') #mostra o nome e o curso de cada aluno no dicionário
    print('-' * 20)