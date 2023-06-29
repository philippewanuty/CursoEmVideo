'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão 
de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('{:*^40}'.format('Progressão aritimetica'))

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + 10 * razao #formula
print(decimo)

'''#primeira forma

while not termo == decimo :
    print('{} →'. format(termo), end = ' ')
    termo +=  razao

print('fim')'''

#segunda forma

cont = 1
while cont <= 10:
     print('{} →'. format(termo), end = ' ')
     termo += razao
     cont += 1

print('fim')