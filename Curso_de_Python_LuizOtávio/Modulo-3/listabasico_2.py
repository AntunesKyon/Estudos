lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

lista = ['Mario', 'João', 'Kaio']

for nome in lista:
    print(nome)

indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice])