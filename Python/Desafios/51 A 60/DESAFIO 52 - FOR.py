'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

print('Verificador de numero primo')
total=0
numero = int(input('Digite um numero: '))
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[31m', end=' ') # cores no python
        total = total+ 1
    else:
        print('\033[33m', end=' ')
    print(' {} '.format(c), end=' ')
if total == 2:
    print(' \nO numero {} é primo.'.format(numero))
else:
    print(' \nO numero {} NÃO é primo.'.format(numero))


# tive dificuldades mas entendi