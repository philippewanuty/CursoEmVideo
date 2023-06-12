#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite o seu nome completo? ').strip()
# nome = 'JOAO SILVA'

print('O nome informado foi: {}'.format(nome.title()))
veri = 'silva' in nome.lower()

print('No nome informado contém Silva? ', veri)

#DESAFIO 025 - FINALIZADO - CORRETO