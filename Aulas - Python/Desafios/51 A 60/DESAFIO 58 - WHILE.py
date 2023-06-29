'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''
import random
from time import sleep
print('IA pensando... ')
sleep(1)

bot = random.randint(0,10)
tentativa = int(input('Qual o número que o computador pensou?: '))
palpite = 0

while bot != tentativa:
    55
    if bot > tentativa:
        print('Mais pra cima...')
    elif bot < tentativa:
        print('Mais pra baixo...')

    tentativa = int(input('Qual o número que o computador pensou?: '))
    palpite +=1
    

print('Haha! Eu pensei o Nº{} até que fim você adivinhou! Você levou {} palpites para acertar'.format(tentativa,palpite))