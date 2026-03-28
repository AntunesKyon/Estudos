frase = 'O python é uma linguagem de Programaçãao ' 'multiparadifma' 'Python foi criado '
i = 0
qtd_apamais_vz = 0
letraqmaisapa = ''
while i<len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i+= 1
        continue

    qtd_aparicoes = frase.count(letra_atual)

    if qtd_apamais_vz < qtd_aparicoes:
        qtd_apamais_vz = qtd_aparicoes
        letraqmaisapa = letra_atual

    i+=1

print(f'A letra que apareceu mais vezes foi {letraqmaisapa} e apareceu {qtd_apamais_vz} vezes')