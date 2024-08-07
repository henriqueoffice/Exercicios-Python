from time import sleep


def maior(*núm):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for v in núm:
        print(v, end=' ')
        sleep (0.2)
    print(f'Foram informados {len(núm)} valores ao todo.')
    for v in núm:
        if núm[0] == 0:
            maior = núm[0]
        else:
            if v > maior:
                maior = v
    print(f'O maior valor informado foi {maior}.')

#Programa Principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
