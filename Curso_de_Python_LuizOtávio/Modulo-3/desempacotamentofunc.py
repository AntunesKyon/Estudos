string = 'ABC'
lista = ['Maria','Helena',1,2,3,'Eduarda']
tupla = 'Python', 'é', 'legal'

m, h, *_, t, e = lista#pega os elementos 0 1 da lista e os dois ultimos
print(m, e, t)

print('Maria','Helena',1,2,3,'Eduarda')
print(*lista)

salas = [
    #[0] Indice da Lista e temos os indice dos objetos dentro que são [0][1]
    ['Maria', 'Jose',],
    #[1][0]
   ['Jade',],
    #[2][0][1][2]
    ['Luiz', 'João', 'Eduarda',(0,10,20,30,40)],

]
print(*salas, sep='\n')