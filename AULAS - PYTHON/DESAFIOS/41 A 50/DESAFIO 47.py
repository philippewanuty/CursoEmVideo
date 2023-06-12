'''Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão
 no intervalo entre 1 e 50.'''

print('Numeros pares de 1 a 50')

for x in range (2, 51, 2):
    print('Nº:{}'.format(x), end = ' ')
print('Fim do código')


# TIPS: ESSE end = ' ' é usado para imprimir lado a lado o resultado, onde dentro do parenteses fica o espaço