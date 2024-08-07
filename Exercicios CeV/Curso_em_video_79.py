
'''controle = True
lista = []

while controle == True:
    e = int(input("Digite o valor que quer adicionar: "))
    for c in lista:
        if lista[c] == e:
            print("Este valor já foi digitado")
        else:
            lista.append(e)    
    sair = input("Deseja terminar [s/n]: ")
    if sair == "s":
        controle = False
print(f'Os números digitados foram {lista}.')
'''


numeros = []

while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso")
    else:
        print("Valor duplicado. Não vou adicionar...")
    r = str(input("Quer continar? [s/n]: "))
    if r in 'Nn':
        break
print('=-' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')

