'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''

print('-'*22)
print('Sequencia de Fibonacci')
print('-'*22)


t = int(input('Digite termos da Fibonacci deseja mostrar: '))
t1 = 0
t2 = 1
c = 3
print('{} -> {} -> '.format(t1, t2), end ='')
while c <= t:
    t3 = t1 + t2
    print('{} -> '.format(t3), end= '')
    t1 = t2
    t2 = t3
    c += 1

print('fim do código')
