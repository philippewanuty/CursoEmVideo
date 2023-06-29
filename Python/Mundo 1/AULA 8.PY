# AULA 08 - MODULOS

#MATH

import math
import random

'''
n = int(input('Digite um numero: '))
raiz = math.sqrt(n)

print('a Raiz de {} é igual a {}'.format(n, math.ceil(raiz)))   # ARREDONDANDO PRA CIMA
print('a Raiz de {} é igual a {}'.format(n, raiz))
print('a Raiz de {} é igual a {:.2f}'.format(n, raiz)) # ARREDONDANDO PRA CIMA COM A FUNÇÃO DO PRINT
'''

#RANDOM
num = random.randint(25,30)
print('O numero escolhido alatóriamente foi {} e a sua raiz é {:.2f}'.format(num, math.sqrt(num)))



#TIPS

#APERTANDO CTRL+SPACE APÓS O 'from math import ' VOCE ABRE A BIBLIOTECA DEMONSTRANDO TODAS AS FUNCIONALIDADES.

# TIPS OURO

# QUANDO VOCE FAZ AS IMPORTAÇÃO ISOLADA PELO 'from' VOCE NÃO PRECISA CHAMAR O MODULO math  ANTES DA FUNÇÃO.
# PORQUE SÓ VAI EXISTIR ELE, OU SEJA VOCE SÓ PRECISA CHAMAR A FUNCAO, ISSO VALE PRA QUANTAS FUNCOES VOCE DESEJA CHAMAR PELO FROM