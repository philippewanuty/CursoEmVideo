'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('='*30)
print('{:^30}'.format('BANCO DO PHILIPPE'))
print('='*30)

valor = int(input('Qual o valor será sacado ? '))
cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0


while True:

    if valor >= 50:
        valor -= 50
        cont50 += 1
    else: 
        if valor >= 20:
            valor -= 20
            cont20 += 1
        else:
           if valor >= 10:
               valor -= 10
               cont10 += 1
           else:
                if valor >= 1:
                    valor -= 1
                    cont1 += 1
                else:
                    break    
print('='*30)          
print(f'''Dinheiro R$:{valor}
Quantidade de notas de 50: {cont50}
Quantidade de notas de 20: {cont20}
Quantidade de notas de 10: {cont10}
Quantidade de notas de 1: {cont1}''')
