#EXERCÍCIO PYTHON 018: FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO.
import math

ang = float(input('Digite um ângulo para saber o seno, cosseno e tangente deste ângulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('O Angulo proposto foi {} Abaixo estarão os resultados: \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(ang, seno, cosseno, tangente))



#FIM DO CÓDIGO

