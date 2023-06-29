'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''


pergunta = 'S'
contidade = 0
contsexo = 0
cont20 = 0

while True:

    idade = int(input('Infome a sua idade: '))
    sexo = str(input('Informe o seu sexo: [ H ou M]: ')).upper()
    pergunta = str(input('Deseja continuar ? [S ou N]: ').strip().upper())[0]
    if idade > 18 :
        contidade += 1
    if sexo == 'H':
        contsexo += 1
    if sexo == 'M' and idade < 20:
        cont20 += 1
    if pergunta == 'N':
        break


print(f'Existem {contidade} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {contsexo} homens.')
print(f'Existem {cont20} mulheres com menos de 20 anos')