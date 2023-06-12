# EXERCÍCIO PYTHON 035: DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.

print('Digite as 3 retas para formar um triangulo')


r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))

print('Retas informadas: {},{}, {}'.format(r1,r2,r3))


if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:

    print('é {}possivel {}formar um triangulo'.format(cores['azul'],cores['limpar']))

else:
    print('é impossivel formar um triangulo')

print('Fim.')

#FIM DO CÓDIGO