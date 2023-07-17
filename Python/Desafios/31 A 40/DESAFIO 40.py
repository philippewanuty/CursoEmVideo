'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO 

'''

print('Caro aluno para saber o resultado da sua aprovação por gentileza informe as suas notas. ')

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1+n2)/2

print('Sua nota N1: {}\nSua nota N2: {}\nSua Media: {}' .format(n1,n2,media))

if media < 5:
    print(('Você não alcançou a nota suficiente para aprovação, você foi REPROVADO'))
elif media >= 5 and media < 7:
    print('Sua nota não foi suficiente para aprovação, voce está em RECUPERAÇÃO')
elif media >= 7:
    print('Parabéns voce foi APROVADO, pode comemorar!')
else: print('Porque estou aqui ?')

print('Fim do programa.')