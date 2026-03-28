while True:

    num1 =  input("Digite um número: ")
    num2 =  input("Digite um outro número: ")
    operador = input("Digite uma operador: ")

    numeros_validos=None

    num1_float = float(num1)
    num2_float = float(num2)

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados não são validos. ')
        continue

############################################################################
    operador_permitidos = '+-/*'

    if operador not in operador_permitidos:
        print("O operador que você tentou utilizar não está entre os permitidos")


    if len(operador)> 1:
        print('Digite apenas um operador')
        continue
#######################################################################################
    if operador == '+':
        soma = num1_float + num2_float
        print(soma)
    elif operador == '-':
        subtracao = num1_float - num2_float
        print(subtracao)
    elif operador == '*':
        multiplicacao = num1_float * num2_float
        print(multiplicacao)
    elif operador == '/':
        divisao = num1_float / num2_float
        print(divisao)
    else:
        print("Erro na operador")

######################################################################################
    sair = input("Você que sair? [S/N]").upper().startswith('S')
    if sair == "S":
        break

