'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

print('{:+^40}'.format('Programa de Velhice'))

ano = 0
maior = 0
menor = 0

for contagem in range(1, 8):
    ano = int(input('Olá, em que ano a {}º pessoa nasceu?: '.format(contagem)))
    print(ano)
    if ano <= 2005:
        maior += 1
    else:
        menor += 1

print('Ao total {} pessoas são de maioridade e {} pessoas são de menor idade'.format(maior,menor))