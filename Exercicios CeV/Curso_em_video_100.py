from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0,5):
        valor = randint(1,10)
        lista.append(valor)
        sleep(0.3)
        print(f'{valor} ', end='')
    print('PRONTO')

def somapar(lista):
    soma = 0
    for n in lista:
        if n%2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')


# Programa Principal
números = []
sorteia(números)
somapar(números)
