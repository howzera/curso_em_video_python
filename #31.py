N = int(input('Digite a distancia da sua viage'))

if N <= 200:
    print('Valor da passagem: R$ {:.2f}'.format(N*0.50))
else:
    print('Valor da passagem: R$ {:.2f}'.format(N*0.45))