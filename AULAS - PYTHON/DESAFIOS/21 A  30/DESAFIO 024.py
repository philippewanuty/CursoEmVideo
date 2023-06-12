#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: ')).strip()

#cidade = 'SANTO ANTONIO'

lista = cidade.split()

print ('O nome da cidade é {}'.format(cidade.title()))

contagem = 'santo' in lista[0].lower()

print('O nome da cidade começa com "Santo" ? ', contagem)


'''
if contagem == true :

    print('A primeira palavra começa com SANTO')

else :
    print('A palvra não começa com SANTO')
'''




#DESAFIO 024 - FINALIZADO


#Correto porém o professor resolveu de maneira diferente.







