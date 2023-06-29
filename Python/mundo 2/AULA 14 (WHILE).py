# WHILE - ENQUANTO - ESTRUTURA DE REPETIÇÃO COM TESTE LOGICO
'''As duas funções podem ser usadas para a mesma situação, porém voce deve usar o while quando não
souber o limite.'''

'''for c in range( 10, 110, 10): #A mesma situação usando o FOR
    print(c)
print('Fim')'''

'''n = 10
while n < 100: # A mesma situação usando o while
    n+=10
    print (n)

print('fim')'''
c = 0
n = ''
while n != 'n':
    n = str(input('Deseja continuar ? [S/N]: '))
    c += 1
    print(c)
print('O numero terminou em {}'.format(c))





