#AULA 6 - VÍDEO 06

#Tipos primitivos

'''
INT - NUMEROS INTEIROS ( 7 , -4 , 0 , 1235)
FLOAT - NUMEROS REAIS OU FLUTUANTES ( 4.5 , 0.076 , -15.223, 7.0)
BOOL - VALORES LOGICOS ( True, False)
STR - LETRAS ( 'Olá' , '7.5', '')

'''
#FUNÇÃO FORMAT ('xyz'.format(x,x,x))

'''
n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
soma = n1+n2

print('a soma entre {} e {} é {}' .format(n1, n2, soma))

'''
#TIPS


# NESSA AULA O PROFESSOR COMENTOU SOBRE O METODO DE TESTE DE TIPO, O "É ALGUMA COISA" EX:  (xyz.isxxx())
# ALGUNS EXEMPLOS (.isnumeric, .isalpha, .isalnum) ..
# COMENTOU TAMBÉM SOBRE O METODO DE VERIFICAÇÃO DE DIFITAÇÃO NO INPUT O TYPE. E: abc(type(xyz))

'''
#EX IS
print(soma.isnumeric())
# EX TYPE
print('o tipo é' , type(soma))

'''

#DESAFIO

#FAÇA UM SCRIPT EM PYTHON QUE INFORME ALGUMAS CARÁCTERISTICAS DO QUE É DIGITADO NO METODO INPUT.

'''

digite = (input('Digite algo:'))

print("O tipo primitivo do que foi digitado é :", type(digite))
print("O que foi digitado é numérico?", digite.isnumeric())
print("O que foi digitado é alphabeto?", digite.isalpha())
print("O que foi digitado é maiúsculo?", digite.isupper())
print("O que foi digitado é alphanumérico?", digite.isalnum())

'''

#FIM