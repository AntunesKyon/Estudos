nome = input("Digite seu nome:")
idade = input("Digite sua idade: ")
if nome and idade:
    print(f'seu nome é {nome} ')
    print(f'seu nome é {nome[::-1]}')
    if ' ' in nome:
        print("seu nome tem espaços")
    else:
        print("seu nome não tem espaços")
    print(len(nome))
    print((nome[0]))
    print((nome[:-1]))##pegar a ultima letra do nome
else:
    print("Desculpe, você deixou campos vazios")
##resolver pq não ta aparecendo o final quando deixo de digitar a idade
