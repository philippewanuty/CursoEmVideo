'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

print('Seja bem vindo ao programa de seleção de categoria')
idade = int(input('Por favor digite a sua idade: '))

if idade <=9:
    print('Voce tem {} anos e a sua categoria é o MIRIM'.format(idade))
elif idade >9 and idade <=14:
    print('Voce tem {} anos e a sua categoria é o INFANTIL'.format(idade))
elif idade >14 and idade <=19:
    print('Voce tem {} anos e a sua categoria é o JUNIOR'.format(idade))
elif idade >19 and idade <=25:
    print('Voce tem {} anos e a sua categoria é o SENIOR'.format(idade))
elif idade >25:
    print('Voce tem {} anos e a sua categoria é o MASTER'.format(idade))

print('Fim do progama')