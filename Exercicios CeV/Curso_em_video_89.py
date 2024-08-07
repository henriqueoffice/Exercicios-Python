

ficha = list ()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [s/n] '))
    if resp in 'nN':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')


'''
dados = []
nome = list()
notas = []
media = list()
controle = True
cont = 0
n = 0

while controle == True:
    nome = str(input('Aluno: '))
    while cont < 2:
        notas = float(input(f'Nota {cont+1}: '))
        cont = cont + 1
    cont = 0
    media = (notas[0]+notas[1])/2
    n = input('Deseja parar? [s/n] ')
    if n == "s" or n == "S":
        controle = False
    
    dados.append(nome)
    dados.append(notas)
'''
