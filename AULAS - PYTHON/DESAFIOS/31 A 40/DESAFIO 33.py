# EXERCÍCIO PYTHON 033: FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.

print('Digite três numeros inteiros e eu vou te informar qual é o maior e menor em sequencia.')

num1 = int(input('Digite o numero 1: '))
num2 = int(input('Digite o numero 2: '))
num3 = int(input('Digite o numero 3: '))

if num1 > num2 and num1 > num3:
    print('o primeiro numero digitado: {} é o maior.'.format(num1))


if num2 > num1 and num2 > num3:
    print('o segundo numero digitado: {} é o maior.'.format(num2))


if num3 > num1 and num3 > num2:
    print('o terceiro numero digitado: {} é o maior.'.format(num3))


if num1 < num2 and num1 < num3:
    print('o primeiro numero digitado: {} é o menor.'.format(num1))


if num2 < num1 and num2 < num3:
    print('o segundo numero digitado: {} é o menor.'.format(num2))


if num3 < num1 and num3 < num2:
    print('o terceiro numero digitado: {} é o menor.'.format(num3))

print('Fim.')

#FIM DO DESAFIO