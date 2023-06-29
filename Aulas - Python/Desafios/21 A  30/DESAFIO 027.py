#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.


#nome = input('Digite o seu nome completo: ')
nome = 'Philippe Wanuty silva vieira da costa'
lista = nome.split()
ult = len(lista)
print('O seu primeiro e ultimo nome é {} {}'.format(lista[0].capitalize(), lista[ult-1].capitalize()))


#DESAFIO 027 - FINALIZADO - CORRETO





