

matriz = []
par = col3 = mail2 = 0

for l in range(0,3):
    linha = []
    for c in range(0,3):
        linha.append(int(input(f'Digite um valor para [{l},{c}]: ')))
        if linha[c] % 2 == 0:
            par = par + linha[c]
        if c == 2:
            col3 = col3 + linha[c]
#    if l == 1:
        #mail2 = max(linha)

                
        
    matriz.append(linha)

print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {col3}')
for c in range(0,3):
    if c == 0:
        mail2 = matriz[1][c]
    else:
        if matriz[1][c] > mail2:
            mail2 = matriz[1][c]
print(f'O maior valor da segunda linha é {mail2}') 
