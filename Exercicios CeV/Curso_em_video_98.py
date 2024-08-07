from time import sleep

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            sleep(0.2)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(cont, end = ' ')
            sleep(0.2)
            cont -= p
    print('FIM')

    
#Programa Principal
contador(1,10,1)
contador(10,0,2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i,f,p)
