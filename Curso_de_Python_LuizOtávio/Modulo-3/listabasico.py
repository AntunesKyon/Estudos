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
lista.insert(0,5)#a primeira posição se refere ao índice que desejamos colocar e a segunda posição e o valor (caso o valor na segundo posição seja muito grande ele so põem no final caso não exista a posição na lista)
print(lista)
lista.clear()
print(lista)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_c)
lista_a.extend(lista_b)#alterando diretamente a lista a jogando os valores de b em a
print(lista_a)
