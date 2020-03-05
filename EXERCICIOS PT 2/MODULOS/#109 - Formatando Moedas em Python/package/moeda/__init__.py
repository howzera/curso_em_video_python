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
