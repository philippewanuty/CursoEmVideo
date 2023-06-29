'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

soma = 0
contagem = 0

while True:
    numero = int(input('Digite um numero inteiro[para parar digite 999]: '))
    if numero == 999:
        break
    soma += numero
    contagem += 1
   
print(f'A quantidade de numeros digitados foi {contagem} e a soma deles é {soma} ')
print('Fim ')
    