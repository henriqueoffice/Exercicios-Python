'''
def leiaInt(msg):
    while True:
        x = str(input(msg))
        if x.isnumeric():
            break
        else:
            print('ERRO! Digite um número inteiro válido.')
        return int(x)
'''

def leiaInt(a):
    while True:
        valor = str(input(a))
        if valor.isnumeric():
            break
        else:
            print('ERRO! Digite um número válido')
    return int(valor)


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
