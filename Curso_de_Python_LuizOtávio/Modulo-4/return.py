variavel = print("Luiz")
print(variavel)
print(variavel is None)
#todo print tem valor None pq e o valor padrão de uma funcao

def soma(x, y):
    return x + y # neste caso ele retonar o valor padrão neste caso um inteiro
    #return 'termina a função' então se você tentar por algo após ele diz que é inalcancaveu
#se eu tirar o return vota ao None
exemplo = soma(2, 3)
exemplo_2 = soma(3, 5)
print(exemplo+exemplo_2)
print(exemplo)

