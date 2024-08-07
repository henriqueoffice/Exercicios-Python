'''
galera = []
dado = []
totmai = totmen = 0

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
'''

dado = list()
relacao = []
pessoas = 0
controle = True
resp = 0
mai = men = 0


while controle == True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(relacao) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men  = dado[1]
    relacao.append(dado[:])
    pessoas += 1
    dado = []
    resp = input('Deseja continuar? [s/n]')
    if resp == "N" or resp == "n":
        controle = False


print('-=' * 30)
#print(f'Os dados foram {relacao}')
print(f'Foram cadastradas {len(relacao)} pessoas')
print(f'O maior peso foi de {mai}kg. Peso de ',end='')
for p in relacao:
    if p[1] == mai:
        print(f'{p[0]} ',end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ',end='')
for p in relacao:
    if p[1] == men:
        print(f'{p[0]} ',end='')
