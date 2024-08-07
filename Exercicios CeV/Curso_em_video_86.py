

matriz = []

for l in range(0,3):
    linha = []
    for c in range(0,3):
        linha.append(int(input(f'Digite um valor para [{l},{c}]: ')))
    matriz.append(linha)

print('-=' * 30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()
