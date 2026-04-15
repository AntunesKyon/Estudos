x, y, *resto = 1,2,3,4
print(x, y, *resto)

def soma(*args):#empacota tudo que enviar para funçaõ dentro de uma tupla
    total = 0
    for numero in args:
        total += numero
    return total

    #print(args, type(args))

soma(1,2,3)
soma_1_2_3 = soma(1,2,3)

numeros = 1,2,3,4,5,6,7,78,10
outra_soma = soma(*numeros)
print(outra_soma)

#print(sum((1,2,3,4,5,6,7,78,10)))
print(*numeros)#ele desempacota da tupla