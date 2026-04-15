def multiplicar(*args):#empacota tudo que enviar para funçaõ dentro de uma tupla
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)
