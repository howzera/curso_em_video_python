#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final,de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
#https://youtu.be/QuWDyUeoaJs

a = float(input('Digite a primeira nota:'))
b = float(input('Digite a segunda nota:'))

media = (a+b)/2

if media < 5:
    print('Reprovado')
elif media > 5 and media < 6.9:
    print('Recuperação')
elif media >= 7:
    print('Aprovado')
    