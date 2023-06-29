#D015  ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. 
#CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO

d = int(input('Por quantos dias voce ficou com o carro? '))
km = float(input('Por quantos kilometros voce andou? '))
custo = (60 * d) + (0.15 * km)

print('Você andou {} KM e passou {} dias com o carro, o valor a pagar será R$:{:.2f} '.format(d, km, custo))


#DESAFIO CONCLUÍDO