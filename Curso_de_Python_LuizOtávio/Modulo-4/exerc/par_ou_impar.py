def par_impar(num):
    par = num % 2 == 0
    if par:
        return f'{num} par'
    return f'{num} impar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(100))
print(par_impar(16))
