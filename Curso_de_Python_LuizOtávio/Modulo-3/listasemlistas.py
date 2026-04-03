salas = [
    #[0] Indice da Lista e temos os indice dos objetos dentro que são [0][1]
    ['Maria', 'Jose',],
    #[1][0]
   ['Jade',],
    #[2][0][1][2]
    ['Luiz', 'João', 'Eduarda',(0,10,20,30,40)],

]

print(salas[2][1])
print(salas[2][3][1])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
