# iter mostra o iterador
# next mostra o próximo valor que 'estiver disponivel'

texto = iter('luiz')#__iter__() tbm funciona
print(texto.__next__()) #assim com chamar print(next(texto)
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
#ele da erro porque não tem mais nada a se mostrado pela string

while True:
    try:
        print(next(texto))
    except StopIteration:
      break

'''numero =  range(0, 100,8)

for numero in numero:
    print(numero)'''

