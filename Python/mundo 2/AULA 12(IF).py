#CONDIÇÕES ANINHADAS

# if
# elif - pode tem quantos quiser pós o if.
# else - pode ter apenas um else para um if.


nome = str(input('Qual é o seu nome?'))

a= "seu nome começa com a letra a"
b= "seu nome começa com a letra b"
c= "seu nome começa com a letra c"

if nome[0] == 'a':
    print(a)
elif nome[0] == 'b':
    print(b)
elif nome[0] == 'c':
    print(c)

else:
    print('Nome sem letra correspondente.')