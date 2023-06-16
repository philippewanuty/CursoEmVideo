'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''
contador = 0
tabuada = 0
resultado = 0

while True: 
    numero = int(input('Digite um numero para saber sua tabuada: '))
    if numero <= 0:
         break
    for contador in range(1,11): 
        resultado = numero*contador
        print(f'{numero} x {contador} = {resultado}')
    

print('Fim do Código')