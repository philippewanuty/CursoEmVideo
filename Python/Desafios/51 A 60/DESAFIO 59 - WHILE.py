'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
op = '0'

while op != 5:
    print('\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    op = int(input('\n-> Digite uma das opçôes: '))

    # Somar
    if op == 1:
        soma = n1 + n2
        print(' \nResultado: A soma entre {} e {} é {}.'.format(n1, n2, soma))

    # Multiplicar
    elif op == 2:
        multi = n1 * n2
        print(' \nResultado: A multiplicação entre {} e {} é {}.'.format(
            n1, n2, multi))

    # Maior
    elif op == 3 and n1 > n2:
        print('\nEntre {} e {} o maior é {}'.format(n1, n2, n1))

    elif op == 3 and n1 < n2:
        print('\nEntre {} e {} o maior é {}'.format(n1, n2, n2))
    elif op == 3 and n1 == n2:
        print('\nOs dois numeros são iguais')

    # Digitar novamente
    elif op == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif op == 5:
        print('Finalizando...')

    # Opção inválida
    else:
        print('Opção inválida, tente novamente.')
    # Sair
print('Progragama finalizado')

#fim do desafio
