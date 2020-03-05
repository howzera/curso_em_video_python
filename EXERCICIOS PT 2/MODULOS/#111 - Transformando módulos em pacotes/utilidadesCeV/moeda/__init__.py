def moeda(n):
    return (f'R$ {n:.2f}')

def aumentar(n, p, opc = False):
    if opc == False:
        y = (p/100) + 1
        x = n * y
        return x
    else:
        y = (p/100) + 1
        x = n * y
        return moeda(x)

def diminuir(n, p,  opc = False):
    if opc == False:
        x = (p/100) * n
        y = n - x
        return y
    else:
        x = (p/100) * n
        y = n - x
        return moeda(y)
    
def dobro(n,  opc = False):
    if opc == False:
        return n * 2
    else: 
        return moeda(n*2)


def metade(n,  opc = False):
    if opc == False:
        m = n / 2
        return m
    else:
        m = n / 2
        return moeda(m)


def resumo(n, p1, p2):
    print('-'*30)
    print(f'{"RESUMO DO VALOR:":^30}')
    print('-'*30)

    print(f'{"PREÇO ANALISADO:":<15}', end='')
    print(f'{moeda(n):>15}')

    print(f'{"DOBRO DO PREÇO:":<15}', end='')
    print(f'{dobro(n, True):>15}')

    print(f'{"METADE DO PREÇO:":<15}', end='')
    print(f'{metade(n, True):>15}')

    print(f'{p1} {"DE AUMENTO:":<15}', end='')
    print(f'{aumentar(n, p1, True):>15}')

    print(f'{p2} {"DE REDUÇÃO:":<15}', end='')
    print(f'{diminuir(n, p2, True):>15}')

