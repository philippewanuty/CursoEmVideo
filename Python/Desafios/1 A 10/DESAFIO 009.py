#D009 FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA (COM OS CONHECIMENTOS ATÉ A AULA 4)

n1 = int(input('Digite um numero inteiro: '))
t1 = n1 * 1
t2 = n1 * 2
t3 = n1 * 3
t4 = n1 * 4
t5 = n1 * 5
t6 = n1 * 6
t7 = n1 * 7
t8 = n1 * 8
t9 = n1 * 9
t10 = n1 * 10
 
print('o numero digitado foi {} \nE abaixo está sua tabuada.'.format(n1))
print('-------------------------------------')
print('{} x {:2} = {}'.format(n1, 1, t1))
print('{} x {:2} = {}'.format(n1, 2, t2))
print('{} x {:2} = {}'.format(n1, 3, t3))
print('{} x {:2} = {}'.format(n1, 4, t4))
print('{} x {:2} = {}'.format(n1, 5, t5))
print('{} x {:2} = {}'.format(n1, 6, t6))
print('{} x {:2} = {}'.format(n1, 7, t7))
print('{} x {:2} = {}'.format(n1, 8, t8))
print('{} x {:2} = {}'.format(n1, 9, t9))
print('{} x {:2} = {}'.format(n1, 10, t10))


print('-------------------------------------')

#DESAFIO CONCLUIDO.

#tips

# NO CÓDIGO QUANDO VOCE QUER QUE OS NUMEROS FIQUEM ENFILEIRADOS COLOCA-SE {:X} ONDE X É UM NUMERO INTEIRO, ISSO FAZ COM QUE ELE SE COMPORTE COMO SE FOSSE UM NUMERO DE 2 ALGARISMOS.