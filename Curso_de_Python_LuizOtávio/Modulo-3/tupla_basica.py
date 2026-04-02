nomes = 'Maria', 'Helena', 'Luiz'#Enquanto lista são mutaveis tuplas não
print(nomes) # e tuplas são mais rápidas
print(nomes[1])

nomes2 = ['Maria', 'Helena', 'Luiz']
nomes2 = tuple(nomes2)#convertendo lista para tupla
nomes2 = list(nomes2)#convertendo de tupla para lista
print(nomes2)