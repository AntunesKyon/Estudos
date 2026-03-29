'''string =  'ABCDE'
lista = [123, True, 'Luiz Otávio', 1.2, []]
lista[-3] = 'Joaquim'
print(lista[2].upper(), type(lista[2]))'''

lista = [10, 20, 30, 40, 50,60]
#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])
lista.append(70)
lista.append(80)#pode se add qualquer tipo
ultimovalorremovido = lista.pop()#o pop remove qualquer coisa desde que seja o ultimo antes dele
lista.append(90)
print(lista)
print(lista, 'removido,', ultimovalorremovido )