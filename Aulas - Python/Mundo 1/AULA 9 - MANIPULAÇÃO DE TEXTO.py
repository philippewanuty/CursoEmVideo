# AULA 9 - MANIPULAÇÃO DE CADEIAS DE TEXTO

# CADEIDA DE CARÁCTERES É QUALQUER TIPO DE PALAVRA OU FRASE.

#OPERADORES

# FATIAMENTO DE STRING

frase = 'EU SOU LINDO'  # SE TEM 11 CÉLULAS CONTANDO A PARTIR DO ZERO

'''
print('Lendo a sétima celula na cadeida de texto:' + frase[7])
print('lendo da sétima célula té o final na cadeia de texto: ' + frase[7:12])
print('lendo da sétima célula até o final pulando de dois em dois ' + frase[7:12:2])
print('lendo da primeira célula até antes da célula 7: ' + frase[:7])
print('lendo a partir célula 7 até o final: ' + frase[7:])
print('lendo da sétima célula até o final pulando de dois em dois' + frase[7::2])
'''

#ANÁLISE - len() -  VEM DE LENGHT QUE SIGNIFICA COMPRIMENTO.

print('len:', len(frase)) # DA O VALOR DE 12 MAS LEMBRE-SE COMEÇA A CONTAR A PATIR DO ZERO


#CONTAR - count() - CONTAR STRINGS ESPECÍFICADAS EM UMA CADEIDA DE TEXTO

contagem = frase.count('LINDO')
print('count:', contagem)

#ENCONTRAR - find() - ENCONTRA E INFORMA ONDE SE ENCONTRA O COMEÇO DA STRING.

encontrar = frase.find('INDO')
print('find:', encontrar)

#VERIFICAR PRESENÇA - in - USO  'xxxx'in yyyy - VERIFICA SE TEM UMA PALAVRA EM UMA CADEIA DE STRINGS

verificar = 'LINDO' in frase
print('in:', verificar)



#SUBSTITUIÇÃO - replace(xxx, yyy) - SUBISTITUI UMA PALAVRA POR QUALQUER OUTRA.

subs = frase.replace('LINDO','Lindo' )
print('replace:', subs)

#MAIÚSCULO / MINUSCULO -

# upper() - TRANSFORMA TODOS EM MAIÚSCULO
# lower() - TRANSFORMA TODOS EM MINÚSCULO
# capitalize() - TRANSFORMA APENAS A PRIMEIRA LETRA EM MAIÚSCULO
# title() - TRANSFORMA TODAS AS PALAVRAS COM A PRIMEIRA LETRA  EM MAIÚSCULO

cap = frase.capitalize()
print('capitalize: ', cap)

#REMOÇÃO DE ESPAÇOS -   xxxx.strip()

#strip() - REMOVE TODOS OS ESPAÇOS EXCEDENTES NO COMEÇO E NO FINAL DA CADEIA DE STRING
#rstrip() - REMOVE TODOS OS ESPAÇOS DIREITOS EXCEDENTES DA CADEIA DE STRING
#lstrip() - REMOVE TODOS OS ESPAÇOS ESQUERDOS EXCEDENTES DA CADEIA DE STRING

#DIVISÃO - split() - TRANSFORMA CADA PALAVRA EM UMA CADEIA DE STRING PARTINDO DO 0 - N ONDE CADA PALAVRA TAMBÉM SE TORNA UMA NUMERAÇÃO EM UMA LISTA.


div = frase.split()

print('split:',div)
print('split único: ',div[1])

# JUNÇÃO - join() - SUBISTITUI OS ESPAÇOS VAZIOS POR ALGO

print('join: ' + '-'.join(div)) # FOI FEITO O JOIN EM CIMA DO SPLIT(SUBISTITUI OS ESPAÇOS VAZIOS)
print('join puro: ' + ' '.join(frase)) # COLOCA UM CARACTERE ENTRE AS LETRAS



#TIPS

# PARA IMPRIMIR UM TEXTO INTEIRO COM LINHAS QUEBRADAS BASTA COLOCAR O TEXTO DA FORMA COMO ESTÁ E COLOCAR ASPAS DUPLAS 3 VEZES, FECHANDO E ABRINDO """