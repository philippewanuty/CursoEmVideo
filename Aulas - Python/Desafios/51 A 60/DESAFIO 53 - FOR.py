'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA'''

print('identificador de palindromo')

frase = str(input('Digite uma frase para ser decodificada: '))
palavras = frase.split()
juntas = ''.join(palavras)
juntainvertida = ''
print(juntas)

for letra in range(len(juntas)-1,-1, -1): #descobriu a quantidade de caracteres nas palavras e inverteu a ordem

    juntainvertida += juntas[letra] #pegou a quantidade de caracteres invertidos e somou cada letra da palavra
print(juntainvertida)

if juntainvertida == juntas:
    print('A frase é um polindrono!: {}'.format(juntainvertida))
else:
    print('a frase escolhida não é um polindrono.')
