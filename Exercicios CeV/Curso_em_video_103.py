def ficha(jogador="<desconhecido>",gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


#Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    n = "<desconhecido>"
    ficha(n, g)
else:
    ficha(n, g)
