contador = 0

while contador <= 10:
    print(contador)
    contador += 1

print("Acabou")
################################################
while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')

#####################################################

qtd_linha = 5
qtd_coluna = 5
linha = 1


while linha<qtd_linha:
    coluna = 1
    while coluna<=qtd_coluna:
        print(linha, coluna)
        coluna += 1
    linha += 1
print('Acabou')