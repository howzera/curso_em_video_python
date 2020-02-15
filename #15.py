KM = float(input('Digite os kilometros rodados: '))
DIAS = int(input('Por quantos dias o carro foi utilizado: '))

CUSTOKM = KM*0.15
DIARIA = DIAS * 60
TOTAL = CUSTOKM + DIARIA

print('O total a pagar pelo aluguel do carro é: R$ {:.2f}' .format((TOTAL)))