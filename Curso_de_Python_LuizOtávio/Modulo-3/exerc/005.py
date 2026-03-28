nome = 'João Vitor'
#resultado = "*".join(nome) + "*"
#print(resultado)

indice = 0
nome_remaster = ''
while indice<len(nome):
    letra = nome[indice]+"*"
    nome_remaster += letra
    indice +=1
print(nome_remaster)