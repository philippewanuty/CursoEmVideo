#D010 CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR ( CONSIDERE 1 USD = R$ 3.27)

r = float(input('Quanto reais e quantos centavos voce tem na carteira ? '))
d = r / 3.27

print('Com R${} reais voce pode comprar USD${:.2f} dolares'.format(r, d))

#DESAFICO CONCLUÍDO