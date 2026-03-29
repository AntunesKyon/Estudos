palavra_secreta = 'gato'
letras_acer = ''
n_tentativas = 0

import os

while True:

    n_tentativas +=1
    letra_digitadas = input('Digite uma letra: ')

    if len(letra_digitadas)>1:
        print('Digite somente uma letras')
        continue


    if letra_digitadas in palavra_secreta:
        letras_acer += letra_digitadas

    palavra_formada = ''
    for letra_secrt in palavra_secreta:
        if letra_secrt in letras_acer:
          palavra_formada += letra_secrt
        else:
            palavra_formada +='*'

    os.system('cls')#mudavel 
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        print(f'Você Ganhou !!! a palavra era {palavra_secreta}')
        print(f'O número de tentativas foi {n_tentativas}')

