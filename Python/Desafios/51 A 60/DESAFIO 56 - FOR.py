'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
  e quantas mulheres têm menos de 20 anos.'''


contagem = 0
media = 0
nvelho = ''
idadev = 0


for p in range(1,5):

    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

  #  print('idadev: {}, nomev: {} '. format(idadev, nvelho))


    media = media + idade # media do grupo

    if p == 1 and sexo in 'Mm':
        nvelho = nome
        idadev = idade

    if sexo in 'Mm' and idade > idadev:  # informa o homem mais velho
         nvelho = nome
         idadev = idade

    if  sexo in 'Ff' and idade < 20: # informa meninas abaixo de 20 anos
        contagem = contagem+1

print('A medida da idade do grupo é: {}'.format(media/4))
print('O nome do homem mais velho é: {} e sua idade é {}'.format(nvelho, idadev))
print('Existem {} mulheres com menos de 20 anos'.format(contagem))
