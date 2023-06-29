''' Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
a) O nome com todas as letras maiúsculas e minúsculas.
b) Quantas letras ao todo (sem considerar espaços).
c) Quantas letra s tem o primeiro nome.'''

nome = input('Digite seu nome completo: ')

#nome = 'Philippe Wanuty Silva Vieira da Costa'
nome_ma = nome.upper()
nome_mi = nome.lower()

#a)

print('Nome com todas as letras maiúsculas: ', nome_ma)
print('Nome com todas as letras minúsculas:',nome_mi)

print('')

#b)

lista = nome.split()
sem = ''.join(lista)

print('A palavra contém {} letras sem considerar os espaços.'.format(len(sem)))

#c)

contagem = len(lista[0].lower())

print('Existem {} letras  no primeiro nome.'.format(contagem))


#FIM DO DESAFIO 22

