'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão
 de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

print('{:*^40}'.format('Progressão aritimetica'))

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 * razao) #formula da p.a
print(decimo)

for n in range(termo,decimo,razao):


    print('{} →'. format(n), end = ' ')

print('fim')