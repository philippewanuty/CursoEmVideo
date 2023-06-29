#EXERCÍCIO PYTHON 017: FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO. CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.
import math
intro = input('Programa de calculo de Hipotenusa de um triângulo retângulo.')
cateto_op = float(input('Digite o cateto oposto: '))
cateto_adj = float(input('Digite o cateto adjacente:'))
# hipo = (math.pow (cateto_op, 2)) + (math.pow (cateto_adj, 2)) #SOLUÇÃO FEITA POR MIM
hipo = math.hypot(cateto_op, cateto_adj) #FORMA DE CALCULAR HIPOTENUSA PELO math

print('O Cateto oposto é: {} \nO cato adjacente é: {}'.format(cateto_op, cateto_adj))
print('O valor da hipotenusa é {:.2f}'.format(hipo))


#FIM DO CÓDIGO


