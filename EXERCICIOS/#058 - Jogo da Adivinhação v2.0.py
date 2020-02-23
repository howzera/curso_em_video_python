#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
#https://youtu.be/-QkOIHJ1Chw


from random import randint

cpu = randint(0,10)
totchute = 0
chute = -1
print(cpu)
acertou = False

while not acertou:
    
    chute = int(input('Digite um valor: '))

    if chute == cpu:
        print('Você acertou, Chute = {} Maquina = {}'.format(chute,cpu))
        acertou = True
    else:
        print('Você errou, tente novamente')
        totchute += 1
        
        if cpu > chute:
            print('MAIS....')
        elif cpu < chute:
            print('MENOS...')


print('Você acertou depois de {} tentativas.'.format(totchute))
