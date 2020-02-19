#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
#https://youtu.be/1OFp_-R2B2A

from random import randint

n = cont = 0

while True:

    cpu = randint(0, 10)

    n = int(input('Digite um valor entre 1 e 10: '))
    escolha = str(input('Você quer PAR ou ÍMPAR? [P/I] \n ► ')).upper()

    if escolha in 'Pp':
        
        if (cpu + n)%2 == 0:
            print(f'A soma entre {cpu} e {n} é PAR, você \033[1,32mVENCEU!!!\033[m')
            cont += 1
        else:
            print(f'A soma entre {cpu} e {n} é ÍMPAR você \033[1,31mPERDEU!!!\033[m')
            break

    if escolha in 'Ii':
        
        if (cpu + n)%2 == 0:
            print(f'A soma entre {cpu} e {n} é PAR, você \033[1,31mPERDEU!!!\033[m')
            break
        else:
            print(f'A soma entre {cpu} e {n} é ÍMPAR você \033[1,32mVENCEU!!!\033[m')
            cont += 1

print(f'FIM DO JOGO! VOCÊ VENCEU {cont} RODADAS')
            






