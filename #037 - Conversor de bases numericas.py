#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.
#https://youtu.be/B3F0IjH5WAM

n = int(input('Digite um número: '))

print("""Digite uma das opções se:
        1 - Deseja converter \033[1;36m{}\033[m em binário
        2 - Deseja converter \033[1;36m{}\033[m em octal
        3 - Deseja converter \033[1;36m{}\033[m em hexadecimal""".format(n,n,n))
        
p = int(input('Opção: '))

if p == 1:
    print('O valor \033[1;36m{}\033[m convertido em binário é: {}'.format(n, bin(n)[2:]))

elif p == 2:
    print('O valor \033[1;36m{}\033[m convertido em octal é: {}'.format(n, oct(n)[2:]))

elif p == 3:
    print('O valor \033[1;36m{}\033[m convertido em hexadecimal é: {}'.format(n, hex(n)[2:]))
else:
    print('\033[1;31mERRO:\033[mA opção escolhida não existe')