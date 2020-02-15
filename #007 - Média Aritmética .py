#EXIBIR MÉDIA DE DUAS NOTAS
#https://youtu.be/mqcNw_dhl8I
#Adicionar cores

N1 = float(input('Digite sua primeira nota: '))
N2 = float(input('Digite sua segunda nota: '))

MEDIA = (N1 + N2)/2

print('Sua média é: \033[1;33m{}\033[m'.format(MEDIA))
