#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.


frase = input('Digite uma frase de amor: ').strip()
#frase  = 'Deus é o meu refúgio e a minha fortaleza, nele eu confiarei!'

cont = frase.lower().count('a')

print('A letra "A" aparece {} vezes na frase informada.'.format(cont))

prim = frase.lower().find('a')
ult = frase.lower().rfind('a')

print('A celula onde a letra "A" foi encontrada a primeira vez foi {} '.format(prim+1))
print('A celula onde a letra "A" foi encontrada a ultima vez foi {}'.format(ult+1))

#DESAFIO 026 - FINALIZADO - CORRETO