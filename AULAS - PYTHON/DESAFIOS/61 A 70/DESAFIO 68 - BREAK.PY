'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random

print('{:-^40}'.format('Jogo Par ou Impar'))
escolha_comp = ['par','impar']
escolha = str(input('Digite sua opção[Impar ou Par]: '))
numero = int(input('Digite seu numero: '))
comp_escolha = random.choice(escolha_comp)
comp_numero = random.randint(0,10)
soma_numeros = numero + comp_numero
parouimpa = soma_numeros % 2
resultado = ''


if parouimpa == 0:
    resultado = 'par'
else:
    resultado = 'impar'

if resultado == comp_escolha:
    print(f'Deu {resultado.upper()} o Computador ganhou!')
else:
    print(f'Deu {resultado.upper()} você ganhou!')



print('-'*30)

print(f'O resultado é {resultado}')
print(f'O computador escolheu {comp_escolha} e o numero: {comp_numero}')
print(f'O jogador escolheu {escolha} e o numero {numero}')

