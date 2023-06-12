'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

'''
print('{:+^40}'.format('Somador de numeros pares'))
numero = 0
soma = 0
for n in range(0,6):
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 == 0 : #todo numero dividido por 2 com resto 0 é par
        soma += numero


print(soma)

# fim do exercício, sem dificuldades.