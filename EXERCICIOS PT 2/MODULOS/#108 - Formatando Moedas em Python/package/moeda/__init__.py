def aumentar(n = 0, p = 0):
    y = (p/100) + 1
    x = n * y
    return x


def diminuir(n = 0, p = 0):
    x = (p/100) * n
    y = n - x
    return y

    
def dobro(n = 0):
    return n * 2


def metade(n = 0):
    m = n / 2
    return m

def moeda(n = 0):
    return (f'R$ {n:.2f}'.replace('.',','))