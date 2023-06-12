# EXERCÍCIO PYTHON 020: O MESMO PROFESSOR DO DESAFIO 019 QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.


import random

#COM INPUT


a1 = 'Jeffersom'
a2 = 'Philippe'
a3 = 'Jeová'
a4 = 'Joab'

escolha = [a1, a2, a3, a4]
random.shuffle(escolha)


print('Lista de sorteio para apagar o quadro de hoje, nomes: \n1 - {} \n2 - {} \n3 - {} \n4 - {} '.format(a1, a2, a3, a4))
print('')
print('A ordem de apresentação será: {}'.format(escolha))

print('A ordem de apresentação será: {}'.format(random.sample(escolha, k=2))) #O USO DO sample É BOM PARA ESCOLHER UMA QUANTIDADE ESPECÍFICA DENTROD E UM TODO.


#FIM DO CÓDIGO - CORRETO