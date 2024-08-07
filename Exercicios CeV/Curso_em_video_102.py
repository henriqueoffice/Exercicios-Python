def fatorial(num=1, show=False):
    """
    Fatorial(num, show=False)
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :Return: O valor do Fatorial de um númeo num.
    """
    f = 1
    for c in range(num,0,-1):
        f *= c
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
    return f
