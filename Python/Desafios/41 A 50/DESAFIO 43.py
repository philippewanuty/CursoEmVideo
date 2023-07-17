'''Exercício Python 43:  Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

print('Calculador de IMC')

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.2f}  você está Abaixo do Peso '.format(imc))
elif imc >= 18.5 and imc <= 25 :
    print('Seu IMC é {:.2f}  você está no peso ideal '.format(imc))
elif imc >= 25 and imc <= 30 :
    print('Seu IMC é {:.2f}  você está com sobrepeso '.format(imc))
elif imc >= 30 and imc  <= 40 :
    print('Seu IMC é {:.2f}  você está com obesidade '.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.2f} você está com obesidade morbida '.format(imc))