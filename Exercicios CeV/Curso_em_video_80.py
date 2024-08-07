'''
numeros = []



for n in range (0,5):
    numero = int(input("Digite um valor: "))
    if numero <= numeros[n]:
        numeros.insert(n,numero)
        if numero > numeros[n]:
            numeros.insert(-1,numero)

print(f'Os números digitados fora: {numeros}')
'''

lista = []

for c in range (0,5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("Adicionado na posição final da lista")
    else :
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert (pos,n)
                print(f'Número inserido na posição {pos}')
                break
            pos = pos + 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
