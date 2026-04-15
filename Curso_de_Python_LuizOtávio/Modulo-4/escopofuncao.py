x=1 #pode definir a função

def escopo():
    #global x #| Permite que o x de fora da função seja editado dentro da função
    x = 10
    def outra_funcao():
        #global x
        x=11
        y=2# só pode usar essa função se chamar por ela dentro da função 'original'
        print(x,y)
    #x = 1
    outra_funcao()
    print(x)
#se eu criar uma variavel dentro da função por mais que exista outra função com o mesmo nome dentro do programa não da erro
#print(x) da erro pq x não está definido fora da função
print(x)#printa o x original definido fora da função
escopo()
print(x)

#pelo que entendi toda vez que ele chamamos uma função ela cria um novo espaço na mémoria criando um modulo para armazenar os valores e devolvelos depois