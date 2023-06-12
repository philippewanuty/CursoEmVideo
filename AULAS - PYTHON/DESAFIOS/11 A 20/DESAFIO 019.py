# EXERCÍCIO PYTHON 019: UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DOS ALUNOS E ESCREVENDO NA TELA O NOME DO ESCOLHIDO.
import random

#COM INPUT

'''
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')

escolha = random.choice([a1, a2, a3, a4])


print('Lista de sorteio para apagar o quadro de hoje, nomes: \n1 - {} \n2 - {} \n3 - {} \n4 - {} '.format(a1, a2, a3, a4))
print('')
print('O aluno escolhido de hoje foi: {}'.format(escolha))

'''
#SEM INPUT

a1 = 'Jeffersom'
a2 = 'Philippe'
a3 = 'Jeová'
a4 = 'Joab'
lista = [a1, a2, a3, a4]
escolha = random.choice(lista)  #UMA LISTA SEMPRE ESTARÁ ENTRE COLCHETES

print('Lista de sorteio para apagar o quadro de hoje, nomes: \n1 - {} \n2 - {} \n3 - {} \n4 - {} '.format(a1, a2, a3, a4))
print('')
print('O aluno escolhido de hoje foi: {}'.format(escolha))