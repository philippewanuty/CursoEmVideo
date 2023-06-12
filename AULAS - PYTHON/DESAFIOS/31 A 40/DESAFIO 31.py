# EXERCÍCIO PYTHON 031: DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$0,45 PARTA VIAGENS MAIS LONGAS.

km = int(input('Qual é a distancia da sua viagem? '))

if km <= 200:
    print('O valor por km é 0.50 e o total da  sua viagem será {}'.format(km*0.50))

else:
    print('O valor por km é 0.45 e o total da  sua viagem será {}'.format(km * 0.50))


print('Fim')

#FIM DO DESAFIO