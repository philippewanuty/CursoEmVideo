'''Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

import time

for x in range (10, -1, -1):
    print('Contagem regressiva.. {} ! '.format(x))
    time.sleep(1)
print('BOOOOOOOOM! FELIZ ANO NOVO!!')

#FIM DO EXERCÍCIO