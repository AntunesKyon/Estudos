frase = '  Olha só que    ,coisa interessante      '
lista_de_palavra_cruas = frase.split(',')#e possivel definir onde vai ser dividindo dizendo onde pode deve ser cortado ','

lista_frases = []
for i, frase in enumerate(lista_de_palavra_cruas):
    lista_frases.append(lista_de_palavra_cruas[i].strip())
print(lista_frases)

'''
strip corta os espaço do meio e do fim .strip()
.rstrip() corta os espaço da direita rstrip, e para cortar o da esquerda .lstrip()
nesse caso o join subistui o paramentro tipo vigula pelo que você quiser
'''

frase_unidas ='-'.join(lista_frases)
print(frase_unidas)