'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

numero = int(input('Digite qualquer tipo de número: '))
contador = 0
somanumeros = 0

while numero != 999:
    contador += 1
    somanumeros += numero
    numero = int(input('Digite qualquer tipo de número: '))
print('Os numeros digitados foram: {}'.format(contador))
print('A soma entre eles foram {}'.format(somanumeros))