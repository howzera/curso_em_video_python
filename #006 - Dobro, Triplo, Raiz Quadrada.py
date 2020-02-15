#Exibir o Dobro, Triplo e raiz quadrada
#https://youtu.be/mqcNw_dhl8I
#Adicionar cores

N = float(input('Digite um numero: '))

DOBRO = N*2
TRIPLO = N*3
RAIZ = N**(1/2)

print('O Dobro do numero digitado é: | R:\033[1;31;40m{}\033[m'.format((DOBRO)))
print('O Triplo do numero digitado é:| R:\033[1;31;40m{}\033[m'.format((TRIPLO)))
print('A Raiz do numero digitado é:  | R:\033[1;31;40m{:.3f}\033[m'.format((RAIZ)))
