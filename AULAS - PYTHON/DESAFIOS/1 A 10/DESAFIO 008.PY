#D008 ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS.


n1 = int(input('Digite quantos metros deseja converter: '))
cm = n1 * 100
mm= n1 * 1000

print('{} metros equivalem a: \n{} Centimentros \n{} milimetros.'.format(n1, cm , mm))