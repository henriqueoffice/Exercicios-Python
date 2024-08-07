


aprov = dict()
part=[]
aprov['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {aprov["nome"]} jogou? '))
for p in range(0,partidas):
    part.append(int(input(f'  Quantos gols na partida {p+1}? ')))
aprov['gols'] = part[:]
aprov['total'] = sum(part)
print('-='*30)
print(aprov)
print('-='*30)
for k,v in aprov.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {aprov["nome"]} jogou {partidas} partidas')
for i in range(0,partidas):
    print(f'  => Na partida {i}, fez {part[i]} gols.')
print(f'Foi um total de {aprov["total"]} gols')
