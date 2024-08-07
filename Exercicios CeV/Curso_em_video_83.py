

expr = str(input("Digite a expressão: "))
contabre = 0
contfecha = 0

for n in expr:
    if n == "(":
        contabre = contabre + 1
    if n == ")":
        contfecha = contfecha + 1

if contabre == contfecha:
    print("Sua expressão é válida")
else:
    print("Sua expressão não é válida")
        
