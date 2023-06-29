'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
 No final, mostre qual foi o maior e o menor peso lidos.'''

print('{:*^40}'.format('Contador de peso'))

peso = 0
pesomaior = 0
pesomenor = 0

for c in range(1,6):
    peso = int(input('Digite o peso da {}º pessoa: '.format(c)))

    if c == 1:
        pesomaior = peso
        pesomenor = peso

    if peso < pesomenor :
        pesomenor = peso

    if peso > pesomaior:
        pesomaior = peso



print('O maior peso encontrado foi {} KG \ne o menor peso encontrado foi {} KG'.format(pesomaior, pesomenor))