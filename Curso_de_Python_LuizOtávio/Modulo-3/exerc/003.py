num = int(input("Digite a hora(somente os números :"))

try:
    hora = num
    if  5 <= hora < 12:
        print(f'Bom dia, {hora}!')
    elif 13<= hora >= 17:
        print(f'Boa tarde, {hora}!')
    elif 18<= hora <= 23:
        print(f'Boa noite, {hora}!')
    else:
        print("Hora inválida")
except:
  print("Por favor, digite apenas números inteiros")