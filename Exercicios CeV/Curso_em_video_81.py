

lista = []
controle = True
cont = 0

while controle == True:
    lista.append(int(input("Digite um valor: ")))
    cont = cont + 1
    n = input("Quer continuar? [s/n] ")
    if n == "n":
        controle = False
lista.sort()
lista.reverse()

print("=-" * 30)
print(f'Foram digitados {cont} números')
print(f'Os valores digitados em ordem decrescente são {lista}')

if 5 in lista:
    print("O valor 5 está na lista")
else:
    print("O valor 5 não está na lista")
