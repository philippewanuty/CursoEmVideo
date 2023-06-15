'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''


print('{:*^40}'.format('Progressão aritimetica'))

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1  # quantidade do inicio do termo.
mais = 10 # quantidade de termos que vai terminar
total = 0 # quantidade de termos somados aos novos.
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} →'. format(primeiro), end = ' ')
        primeiro += razao
        cont += 1
    print('Pausa')
    print('Quantidade de termos para começar até o momento {}'.format(cont))
    print('Valor do termo até o momento {}'.format(primeiro))
    mais = int(input('Quantos termos gostaria de mostrar mais?: '))
    
print('voce usou o total de {} termos'.format(total))