'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
totalpreço = 0
produtot = 0
nomepro = ''
produm = 0
cont = 0

while True:
        
    cont += 1
    produtos = str(input('Digite o nome do produto: '))
    preço = int(input('Digite o seu valor R$: '))

    totalpreço += preço
    
    if cont == 1:
        produm = preço
        nomepro = produtos
    if preço < produm:
        produm = preço
        nomepro = produtos

    if preço > 1000:
        produtot += 1

    saida = str(input('Deseja continuar.. [S/N]: ')).strip().upper()[0]
    if saida == 'N':
        break
print('Fim do programa')
print(f'O total gasto na compra foi R$: {totalpreço:.2f}')
print(f'Foram adicionados {produtot} produtos a cima de R$: 1000,00')
print(f'o nome do produto mais barato é {nomepro.upper()} e o seu valor é R$: {produm}')



