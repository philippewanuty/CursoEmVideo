# EXERCÍCIO PYTHON 034: ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
# PARA SALÁRIOS SUPERIORES A R$1250,00, CALCULE UM AUMENTO DE 10%. PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

salario = int(input('Digite o valor do seu salário para receber o aumento:'))

aumento1 = salario+(salario*0.1)
aumento2 = salario+(salario*0.15)

if salario > 1250:
    print('O seu salario era de {:.2f} e teve um aumento de {:.2f} passando a ser {:.2f}.'.format(salario,(aumento1 - salario),aumento1))

else:
    print('O seu salario era de {:.2f} e teve um aumento de {:.2f} passando a ser {:.2f}.'.format(salario, (aumento2 - salario),aumento2))

print('Fim.')

#FIM DO DESAFIO