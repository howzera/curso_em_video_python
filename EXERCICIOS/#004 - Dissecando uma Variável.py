#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
#https://youtu.be/tHYxjJxtJko
#Adicionar cores

ALGO = input('Digite algo: ')

print('{} | Qual tipo primitivo? R: \033[1;32;40m{}\033[m ' .format(ALGO, type(ALGO)))
print('{} | Só tem espaços?      R: \033[1;32;40m{}\033[m ' .format(ALGO, ALGO.isspace()))
print('{} | É um numero?         R: \033[1;32;40m{}\033[m ' .format(ALGO, ALGO.isnumeric()))
print('{} | É alfabético?        R: \033[1;32;40m{}\033[m ' .format(ALGO, ALGO.isalpha()))
print('{} | É alfanumérico?      R: \033[1;32;40m{}\033[m ' .format(ALGO, ALGO.isalnum()))
print('{} | Está em maiusculo?   R: \033[1;32;40m{}\033[m ' .format(ALGO, ALGO.isupper()))
print('{} | Está em minusculo?   R: \033[1;32;40m{}\033[m ' .format(ALGO, ALGO.islower()))
print('{} | Está Capitalizado?   R: \033[1;32;40m{}\033[m ' .format(ALGO, ALGO.istitle()))
