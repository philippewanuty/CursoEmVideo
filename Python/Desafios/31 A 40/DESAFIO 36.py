# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
# do salário ou então o empréstimo será negado.


# APROVAÇÃO DE EMPRESTIMO BANCÁRIO PARA AQUISIÇÃO DE IMÓVEL.

#OBS: FOI ESTIPULADO POR MIM UMA DATA LIMITE DE ANOS (50).
# E O JUROS DO PARCELAMENTO É ZERO

#PERGUNTAS:

#QUAL O VALOR DA CASA?

casa_valor= float(input("Qual o valor da casa que você deseja adquirir? "))

#QUAL O SALÁRIO DO COMPRADOR?

salario_valor = float(input('Qual é o salário do comprador? '))


#EM QUANTOS ANOS ELE VAI PAGAR?

anos= int(input('Em quantos anos deseja pagar? '))
anos_meses=anos*12

#PRESTAÇÃO

prestaçao= casa_valor/anos_meses

#A PRESTAÇÃO NÃO PODE EXECER 30% DO SALÁRIO

if salario_valor*0.3<=(prestaçao):
    print('Para pagar um imóvel de R$:{:.2f} em {} anos a prestação será R$:{:.2f}'.format(casa_valor,anos,prestaçao))
    print('Emprestimo NEGADO!')
else:

     print('Você irá pagar o imóvel de R$:{:.2f} em {} anos e o valor da prestação é {:.2f}'.format(casa_valor,anos, prestaçao))
     print('Parabéns seu financioamento foi APROVADO!')


print('Fim da simulação')

#DESAFIO CONCLUÍDO