# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
#https://youtu.be/ei2Kr3ccfO0


t = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito','Nove', 'Dez', 'Onze',
 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis','Dezessete', 'Dezoito', 'Dezenove', 'Vinte')



while True:

    n = int(input('Digite um valor entre 0 e 20: '))

    if n < 0 or n > 20:
        
        n = int(input('Valor inválido, Digite novamente: '))
    
    else:

        print(f'{t[n]}')

    opc = str(input('Deseja continuar? [S/N]')).upper()

    if opc in 'Nn':
        break

