#METODO DE LISTAS

#append

lista = [1, 2, 3, 4, 5, 5, 5]
lista.append(1)
lista.append('oi')

print(lista)

#insert - INSERE NA LISTA UM NOVO ITEM NA POSIÇÃO DADA

lista.insert(1,7)
print(lista)

#count - CONTA QUANTOS ITENS TEM NA LISTA (ITENS ESPECÍFICOS INDICADOS DENTRO DO PARENTESIS)

contagem = lista.count(1) #CONTA QUANTOS NUMEROS 1 TEM NA LISTA
contagem2 = lista.count(5) #CONTA QUANTOS NUMEROS 5 TEM NA LISTA
print( 'Existem {} numeros 1 na lista'.format(contagem))
print('Existem {} numeros 5 na lista'.format(contagem2))



#pop - imprime e remove o ultimo item da lista
ultimo = lista.pop()

print(ultimo)
print(lista,'Lista retirada o ultimo item')

#sort - ORDENA A LISTA

lista.sort()
print(lista, 'lista ordenada')

#reverse - ordena a lista em ordem reversa

lista.reverse()
print(lista , 'lista em ordem reversa')

#index = retora a posição da primeira ocorrencia do item

print(lista.index(3))

#remove - remove a primeira ocorrencia do item[

lista.remove(1)
print(lista)

#len() - verificar a quantidade de itens em uma lista

print('A quantidade de itens na lista é de: {}'.format(len(lista)))

