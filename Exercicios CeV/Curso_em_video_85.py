
num = [[], []]
valor = 0

for n in range(1,8):
    valor = int(input(f'Digite o {n}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()

print('-=' * 35)
#print(f'Todos os valores {num}')
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
