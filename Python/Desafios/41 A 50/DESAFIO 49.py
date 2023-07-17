'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher
, só que agora utilizando um laço for.

'''

print('{:-^20}'.format('Tabuada'))

numero = int(input('Digite um numero para saber sua tabuada: '))
for n in range(0,11):
    print('{}*{} ={}'.format(numero,n,numero*n))