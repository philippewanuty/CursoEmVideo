#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
import random

# JEITO QUE EU FIZ
'''
num = input('Digite uma sequecia de numeros de 0 a 9999:')

sep = ' '.join(num)

lista = sep.split()

print(num[1])

print('Analizando o numero: {}.'.format(num))

print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {} '.format(lista[3], lista[2], lista[1], lista[0]))
'''


num = int(input('Digite uma sequecia de numeros de 0 a 9999:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10


print('Analizando o numero: {}.'.format(num))

print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {} '.format(u, d, c, m))

#FIM DO CÓDIGO

#OBS - NESSE EXERCÍCIO ELE NÃO USOU NENHUMA FUNÇÃO STRING PASSADA, ELE RESOLVEU COM OPERAÇÕES ARITIMETICAS NATIVAS DO PROGRAMA
# COMO A OPERAÇÃO DIVIDIR INTEIRO // , E DIVIDIR RESTO %


