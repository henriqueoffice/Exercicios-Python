
lista = []
lpar = []
limpar = []
controle = True

while controle == True:
    n = int(input("Digite um número: "))
    lista.append(n)
    c = input("Deseja continuar? [s/n] ")
    
    if n % 2 == 0:
        lpar.append(n)
    else:
        limpar.append(n)

    if c == "n" or c == "N":
        controle = False

print("-=" * 30)
print(f'Os números digitadaos foram {lista}')
print(f'Os números pares digitados são {lpar}')
print(f'Os números ímpares digitados são {limpar}')
