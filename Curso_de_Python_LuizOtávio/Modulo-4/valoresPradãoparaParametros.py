def soma(x,y,z=None):#usar None para quando quiser saber se o valor foi add ou não se fosse zero ele não serviria pq não mostra
    if z is not None:
        print(f'{x=},{ y=},{ z=}', x+y+z)
    else:
        print(f'{x=},{ y=}', x+y)

soma(1,2)
soma(2,3)
soma(100,200)
soma(81, 9, 2)
#Tem a mesma regra de posição caso z fosse o segundo e y o terceiro y teria que ser definido com um valor padrão