pessoa = dict() #semelhante a pessoa = {}
galera = list() #semelhante a galera = []
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        continua = str(input('Quer continuar? [s/n] ')).upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continua == "N":
        break
print('-='*30)
print(f'- Ao todo temos {len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f'- A média de idade é de {média:5.2f} anos.')
print(f'- As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print(' << ENCERRADO >>')
