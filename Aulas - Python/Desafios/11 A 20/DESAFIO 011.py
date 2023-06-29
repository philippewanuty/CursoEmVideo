#D011 FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M²


l = float(input('Qual é a largura da sua parede? '))
a = float(input('Qual é a altura da sua parede ? '))
m2 = l * a

print('Largura da sua parede: {} metros \nAltura da sua parede: {} metros \nMetros quadrados: {} m2'.format(l, a, m2))
print('É necessário {:.1f} litros de tinta para pintar a sua parede'.format(m2 / 2))

#DESAFIO CONCLUÍDO