# EXERCÍCIO PYTHON 016: CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA.

import math
import random

# Num_Real = float(input('Numero Real gerado aleatoriamente:'))

num_real = random.uniform(2.5, 10.00)

print('Numero Real gerado aleatoriamente: {} '.format(num_real))

print('Sua porção inteira é:{}'.format(math.trunc(num_real)))

#FIM DO CÓDIGO