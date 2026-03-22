#try siginifica tentar, então ele tenta aquela opção mas se por a caso aconteça algum erro e não funcionar

#print(1234)
#print(459)
#int('a')
numero_str = input('Vou dobrar o numero que você digitar')

try:
    #print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')



#if numero_str.isdigit():
#else:
#    print('Isso não é u número')


