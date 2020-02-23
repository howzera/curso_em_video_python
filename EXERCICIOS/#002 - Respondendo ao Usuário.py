#Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
#https://www.youtube.com/watch?v=FNqdV5Zb_5Q&
#Adicionar cores

nome = input('Digite seu nome: ')
print("É um prazer te conhecer, \033[1;31;40m{}\033[m!".format(nome))
