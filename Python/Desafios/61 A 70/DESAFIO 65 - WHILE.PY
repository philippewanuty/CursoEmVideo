'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

soma = 0
contagem = 0
numeros = 0
resposta = 's'
numeromaior = 0
numeromenor = 0

while resposta == 's':
    numeros = int(input('Digite quantos numeros inteiros quiser: '))
    soma += numeros
    contagem += 1
    if numeros >= numeromaior:
        numeromaior = numeros
    if numeros >= numeromaior and contagem == 1:
        numeromenor = numeros
    if numeros <= numeromaior and numeros <= numeromenor:
        numeromenor = numeros

    resposta = str(input('Deseja continuar digidanto valores ? [S/N]').lower())
    
print('A medida dos números digitados foi {} '.format(soma/contagem))
print('Seu numero MAIOR foi {} e seu numero MENOR foi {}'.format(numeromaior,numeromenor))
print('Fim do programa')