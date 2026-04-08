def Print(a, b, c):#def nome da função, dentro do () são pârametro
    d = b*c
    print(a, b ,c, d)

Print(1,2,3)#argumentos são valores que devem ser preenchidos conforme os parâmetros da função

def Cumprimento(nome):#(nome = 'Sem nome'): não da erro caso não seja atribuido um pârametro
    print(f'Olá {nome}')

nome = 'Antunes'
Cumprimento(nome)