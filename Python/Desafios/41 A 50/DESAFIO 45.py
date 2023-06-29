#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

print('{:+^40}.'.format(' Jogo JokenPô '))

jogador = (int(input('''Escolha uma das opções: 

0- PEDRA
1- PAPEL
2- TESOURA

Digite sua opção: ''')))

itens = ['pedra', 'papel', 'tesoura']

computador = randint(0,2)


print('+-'*12)
print('IA: {} \nHumano: {}'.format(itens[computador],itens[jogador] ))

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Você ganhou! papel ganha de pedra. ')
    elif jogador == 2:
        print('Você perdeu! Pedra ganha de tesoura. ')
    else:
        print('opção inválida')

elif computador == 1: #computador papel
    if jogador == 0:
        print('Você perdeu! papel ganha de pedra. ')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Você ganhou! tesoura ganha de papel. ')
    else:
        print('opção inválida')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou! pedra ganha de tesoura. ')
    elif jogador == 1:
        print('Você perdeu!, tesoura ganha de papel')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('opção inválida')
else:
    print('Opção errada, fim de jogo')

print('+-'*12)
print('Fim do jogo.')


# resumo do aprendizado:

'''Ele usou a função randint do random, para randomificar os numeros de 0 a 2,
  assim usou a posição da célula na lista usando xxx[yyy]'''


