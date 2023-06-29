'''Exercício Python 48: Faça um programa que calcule a soma entre todos os números
 que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

print('Soma dos multiplos de 3 entre 1 a 500')

count = 0
s = 0
for x in range (1 , 501, 2):
    if x % 3 == 0:
        s = s + x
        x
        count += 1
print('a soma é {} , foram {} valores'.format(s, count))