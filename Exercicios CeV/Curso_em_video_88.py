from random import randint

lista = list()
jogos = []

quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 0


while tot < quant:
    cont = 0
    controle = True
    while controle == True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont == 6:
            controle = False
    lista.sort()
    jogos.append(lista [:])
    lista = []
    tot = tot + 1


print()
print('-=' * 5, f' SORTEANDO {quant} JOGOS ', '-=' * 5)

for i,l in enumerate(jogos):
        print(f'Jogo {i+1}: {l}')


'''
from random import randint
from time import sleep

lista = []
jogos = list()

print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print ('-' * 30)

quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 0

while tot < quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista = []
    tot += 1

print()
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)

for i,l in enumerate(jogos):
    print(f'Jogo {i+1} : {l}')
    sleep(1)

print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
'''
