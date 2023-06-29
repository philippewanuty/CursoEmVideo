'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random

print('{:-^40}'.format('Jogo Par ou Impar'))
escolha = str(input('Digite sua opção[Impar ou Par]: '))
numero = int(input('Digite seu numero: '))
comp_escolha = ''
comp_numero = 0
soma_numeros = 0
parouimpa = 0
resultado = ''
contagem = 0

while True:
    comp_numero = random.randint(0,10)
    soma_numeros = numero + comp_numero
    parouimpa = soma_numeros % 2

    if escolha == 'par':
        comp_escolha = 'impar'
    else:
        comp_escolha = 'par'

    if parouimpa == 0:
        resultado = 'par'
    else:
        resultado = 'impar'

    if resultado == escolha:
        print(f'\nA soma dos numeros foram {soma_numeros} e deu {resultado.upper()} o você ganhou!')
    else:
        print(f'A soma dos numeros foram {soma_numeros} e deu {resultado.upper()} o Computador ganhou!')
        break
    contagem += 1
    print(f'O computador escolheu {comp_escolha.upper()} e o numero: {comp_numero}')
    escolha = str(input('Digite sua opção[Impar ou Par]: '))
    numero = int(input('Digite seu numero: '))



print('-'*30)


print(f'O computador escolheu {comp_escolha.upper()} e o numero: {comp_numero}')
print(f'O jogador escolheu {escolha.upper()} e o numero {numero}')
print(f'o jogador conseguiu ganhar {contagem} vezes seguidas')

# opção mais correta
'''contador = 0
while True:

    numero = int(input('Digite um numero: '))
    numerocomp = random.randint(0,10)
    soma_num = numero+ numerocomp
    escolha = ' '
    
    while escolha not in 'PI':
        escolha = str(input('Escolha par ou impar: [P,I]: ')).strip().upper()[0]
    print(f'seu numero escolhido foi {numero} e o do computador foi {numerocomp}')
    if escolha == 'P':
        if soma_num % 2 == 0:
            print(f'A soma foi {soma_num},e ele é PAR Você GANHOU!')
            contador += 1
        else:
            print(f'A soma foi {soma_num},e ele é IMPAR Você PERDEU!')
            break 
            
    elif escolha == 'I':
        if soma_num % 2 == 0:
            print(f'A soma foi {soma_num},e ele é PAR Você PERDEU!')
            break
        else:
            print(f'A soma foi {soma_num},e ele é IMPAR Você GANHOU!')
            contador += 1
    print('Vamos jogar novamente...')
print(f'Você obteve {contador} Vitórias')'''