# EXERCÍCIO PYTHON 032: FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.

ano = int(input('Digite o ano para descobrir se ele é bissexto: '))

bi = ano % 4

if bi == 0:
    print('O ano informado foi {} e ele é Bissexto, ou seja contém 366 dias.'.format(ano))

else:
    print('O ano informado foi {} não é bissexto e contém 365 dias'.format(ano))

print('Fim.')

#FIM DO DESAFIO