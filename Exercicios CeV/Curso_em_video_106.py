c=('\033[m',        # 0 - sem cores
   '\033[0;30;41m', # 1 - vermelho
   )


def PyHelp(com):
    print(f' Acessando o manual do comando {com} ')
    help(com)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f' {msg} ')
    print('~'*tam)
    print(c[0], end='')

#Programa Principal
comando = ''
título("SISTEMA DE AJUDA PyHELP")
while True:
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        PyHelp(comando)
título('ATÉ LOGO!')

