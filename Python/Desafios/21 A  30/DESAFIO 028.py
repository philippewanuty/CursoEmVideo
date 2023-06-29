# EXERCÍCIO PYTHON 028: ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0 E 5
# E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR. O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.

import random
from time import sleep

bot = random.randint(0, 5)

#usuario = int(input('Oi eu ou seu computador, tente adivinhar o número que eu estou pensando, digite um número de 1 a 5: ' ))
usuario = 2
print('PROCESSANDO...')
sleep(0)
if usuario > 5:
    print('Ah não voce escolheu um numero a cima de 5! não vale!')
else:
    if bot == usuario:
        print('O número que voce escolheu foi {}. \nO numero que o computador pensou foi {}'.format(usuario, bot))
        print('Parabéns voce acertou!')

    else:
        print('O número que voce escolheu foi {}. \nO numero que eu escolhi foi {}'.format(usuario, bot))
        print('Número incorreto, hahaha eu ganhei! tente novamente! :)')

print('Fim do jogo.')


# FIM DO DESAFIO.