'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''

# TIPS
# {:^40} lê-se centralizado em 40 espaços onde o " ^ " significa centralizado.
# entre o : e o ^ pode colocar qualquer caractere para preencher o espaço

#VARIÁVEIS.

print('{:*^40}'.format(' MERCADINHO DO LIPÃO '))

produto = str(input('Qual é o nome do seu produto?: '))
valor = float(input('Qual é o valor do seu produto?: '))
pagamento = int(input('Qual é a sua forma de pagamento? escolha uma opção: \n 1- À vista no dinheiro. \n 2- À vista no cartão. \n 3- Parcelado em até 2x sem juros. \n 4- Parcelado em 3x ou mais com acréscimo. \n'))
pag1 = valor - (valor * 0.1)
pag2 = valor - (valor * 0.05)
pag4 = valor + (valor * 0.2)
forma = 'Opção inválida'
desconto = valor
#CONDIÇÕES

if pagamento == 1:
    desconto = pag1
    forma = 'À vista , Dinheiro -10%'

elif pagamento == 2:
    desconto = pag2
    forma = 'À vista , cartão -5%'
elif pagamento == 3:
    desconto = valor
    forma = 'Parcelado até 2x'
elif pagamento == 4:
    desconto = pag4
    forma = 'Parcelado para mais de 3x com acréscimo'

else:
    print('Opção inválida, digite uma opção de 1 a 4')

#PRINTS

print('O Produto que você está comprando é: {} o seu valor é R$: {:.2f} e sua forma de pagamento é {} e o valor pago será {}'.format(produto,valor,forma,desconto))

