#Exercício Python 39: Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
# do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime


atual = datetime.datetime.now().year


ano = int(input('Qual é o seu ano de nascimento?'))
idade = atual - ano
alistamento= 18
atraso = idade - 18
adiantado = 18 - idade


print('Estamos no ano de {}'.format(atual))

if idade == 18:
    print('Parabéns voce tem {} anos e essa é a idade exata para o alistamento'.format(idade))
elif idade > 18:
        print('Atenção voce tem {} anos e já passou da idade de alistamento, procure uma junta militar'.format(idade))
        print('voce está {} anos atrasado, regularise-se!'.format(atraso))
elif idade < 18:
    print('Você tem {} anos e ainda é jovem para o alistamento militar'.format(idade))
    print('Mas não se preocupe, faltam {} ano(s) para o seu alistamento!'.format(adiantado))

print('fim')

