

nome = str(input("Digite seu nome completo: ")).strip()

print("O nome com letras maiúsculas é: ", nome.upper())
print("O nome com letras minúsculas é: ", nome.lower())
ns = nome.split()
print(f'O nome tem {len(''.join(ns))} letras sem espaço')
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print(f'O primeiro nome é {ns[0]} e ele tem {len(ns[0])} letras')
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
