# EXERCÍCIO PYTHON 029: ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80KM/H,
# MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO. A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.

vel = int(input('Digite a velocidade em que o carro estava: '))

multa = (vel - 80) * 7

if vel > 80:
    print('Você passou a {} KM e ultrapassou a velocidade permitida, sua multa é de R$: {:.2f} '.format(vel, multa))

else:
    print('Você passou a {} KM , a sua velocidade está dentro da faixa permitida.'.format(vel))

print('Fim.')

#FIM DO DESAFIO