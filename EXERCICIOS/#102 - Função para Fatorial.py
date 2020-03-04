# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, # que será um valor lógico (opcional) 
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
# https://youtu.be/84jUX96cs7Q

def fatorial(n, show=False):
    """ -> Calcula o fatorial de um número.
    :parem n: O numero a ser calculado.
    :param show: <opicional>: Mostrar ou não a conta.
    :return: O valor do Fatorial e o numero n: 
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c}', end = ' x ')            
            else:
                print(f'{c}', end = ' = ')
        f *= c
    return f

fatorial(5, True)
help(fatorial)