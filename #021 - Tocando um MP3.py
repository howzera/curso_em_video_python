#Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
#https://youtu.be/9FiEji_fzvk

from pygame import mixer

mixer.init()
mixer.music.load('#21.mp3')
mixer.music.play()
input('Teste')