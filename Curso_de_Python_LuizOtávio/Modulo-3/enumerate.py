
#ENUMERA OS ITENS DA LISTA
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

#lista_enumerada =
#print(next(lista_enumerada))

for item in enumerate(lista, start=19):#faz o indice começar em 19
    print(item)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])