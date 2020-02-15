N = int(input('Digite a velocidade do carro: '))

if N > 80:

    S = N - 80
    print('Você foi multado: R$ {:.2f}'.format(S*7.00))