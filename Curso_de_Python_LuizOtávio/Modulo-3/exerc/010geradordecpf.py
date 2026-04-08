import re

cpf = (input('Digite um cpf: ')).replace('.','').replace('-','').replace(' ','')

cpf =re.sub(r'[^0-9]'),'',cpf

nove_digitos = cpf[:9]
cont_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito)*cont_regressivo
    cont_regressivo -= 1
digito_1 = ((resultado * 10) %11)
digito_1 = digito_1 if digito_1 <=9 else 0

dez_digitos = cpf[:9]+str(digito_1)
cont_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 +=(int(digito)*cont_regressivo_2)
    cont_regressivo_2 -= 1
digito_2 = ((resultado_digito_2 * 10)%11)
digito_2 = digito_2 if digito_2 <=9 else 0

gerado_cpf = f'{nove_digitos}{digito_1}{digito_2}'
print(gerado_cpf)

if cpf == gerado_cpf:
    print(f'{cpf} e válido')
else:
    print('CPF INVÁLIDO')