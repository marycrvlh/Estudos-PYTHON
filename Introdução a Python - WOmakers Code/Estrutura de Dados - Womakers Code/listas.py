#---- LISTA EM PYTHON ----
#os dados dentro de uma lista podem ser alterados ao decorrer do tempo, ou seja, a lista é mutável. Ela é representada por colchetes [] e os elementos são separados por vírgula.

curso = ['python', 'html', 'css', 'javascript']

#imprimindo a lista
print(curso) #mostra a lista completa
print(curso[0]) #mostra o primeiro elemento da lista (python), em programação a contagem começa do zero


#adicionando um dado à lista
curso.append('git e github') #adiciona um novo elemento ao final da lista
print(curso) #mostra a lista atualizada

#adicionando um dado em uma posição específica da lista
curso.insert(1, 'sql') #adiciona um novo elemento na posição 1 da lista (entre python e html)
print(curso) #mostra a lista atualizada

#removendo um dado da lista
curso.remove('css') #remove o elemento 'css' da lista
print(curso) #mostra a lista atualizada

#removendo um dado de uma posição específica da lista
curso.pop(2) #remove o elemento na posição 2 da lista (html)
print(curso) #mostra a lista atualizada