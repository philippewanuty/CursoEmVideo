#D012 FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.

p = float(input('Qual o valor antigo do seu produto? '))
d = p - (0.05*p)

print('O valor do seu produto era {} e com 5% de desconto fica {:.2f}'.format(p, d))

#DESAFIO CONCLUÍDO