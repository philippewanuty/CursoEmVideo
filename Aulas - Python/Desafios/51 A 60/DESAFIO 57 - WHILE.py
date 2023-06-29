'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
 ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

s = str(input('Digite o seu sexo: [M/F]: ')).strip().upper()[0] #strip- tira os espaços #upper - maiúsculo [0] - primeiro carácter

while s != 'M' and s != 'F': # not in 'MmFf' - outra forma certa
    print('Forma incorreta, por favor digite da forma certa conforme o exemplo.')
    s = str(input('Digite o seu sexo: [M/F]: ')).strip().upper()[0]

print('Forma certa, Seu sexo é {}'.format(s))