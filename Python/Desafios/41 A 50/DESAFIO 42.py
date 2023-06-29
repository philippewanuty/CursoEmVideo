'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
 será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''


print('Digite as 3 retas para formar um triangulo')


r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))

print('Retas informadas: {},{},{}'.format(r1,r2,r3))


if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:

    print('É possivel formar um triangulo')

else:
    print('É impossivel formar um triangulo')


if r1 == r2 and r1 == r3:
    print('O Triangulo formado é Equilátero')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('O Triangulo formado é Isóceles')
elif r1 != r2 and r2 != r3 and r1 != r3:
    print('O Triangulo formado é Escaleno')



print('Fim.')