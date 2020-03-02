# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer 
# como parâmetro e mostre uma mensagem com tamanho adaptável.#
# https://youtu.be/Q6basnSo7r0

def escreva(txt):
    l = '~' * (len(txt)+4) 
    print(l)
    print(f'  {txt}')
    print(l)

escreva('Curso em vídeo python')
escreva('OLÁ MUNDO')
escreva('Oi')
