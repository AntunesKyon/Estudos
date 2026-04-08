import os
lista = []

while True:
    opc = input('Selecione uma opção\n[I]nserir [A]pagar [L]istar:')
    if opc == 'I':
        os.system('cls')
        valoradd = input('Digite o que você deseja inserir')
        lista.append(valoradd)
    elif opc == 'A':
        valorapag= input('Digite o item que deseja apagar')
        try:
            indice = int(valorapag)
            del lista[indice]
        except ValueError:
            print('Não e possivel apagar indice')
    elif opc == 'L':
        os.system('cls')
        if lista == []:
            print('Nada a listar')
        for i, valor in enumerate(lista):
            print(i, valor)