# AULA 13 FOR - ITERAÇÃO - ESTRUTURA DE REPETIÇÃO COM VARIÁVEL DE CONTROLE

 ''' EX1: for c in range(0,6, 2): # dentro do parenteses é colocado o inicio, o fim e a iteração (x ,x , i)
    #print(c) # vai imprimir de 0 a 5 de dois em dois '''

#EX2:

s = 0
for x in range (0,4): # o x representa o numero da vez dentro do range
    n = int(input('Digite um número: '))
    s = s+n # ou s += n

print('A somatoria dos números foi {}'.format(s))
