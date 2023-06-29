# EXERCÍCIO PYTHON 030: CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR.


print('Verificação de numero impar ou par')
num = int(input('Digite um numero:'))

resto = num % 2

if resto == 1:
    print('o numero {} é impar'.format(num))

else:
    print('O numero {} é par'.format(num))


print('Fim.')

#FIM DO DESAFIO