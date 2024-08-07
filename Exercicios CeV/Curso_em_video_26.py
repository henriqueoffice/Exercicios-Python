

frase = str(input('Digite uma frase: ')).strip()

print(f'A letra "A" aparece {frase.upper().count("A")} vezes na frase')
print(f'A letra "A" aparece primeiro na posição {frase.upper().find("A")+1}')
print(f'A última letra A Aparece na posição {frase.upper().rfind("A")+1}')
