print('{:^40}'.format('BANCO DO PHILIPPE'))
n= 10
c= 0

while True: 
    if  n == 10:
        n = 9
        c +=1

    elif n == 9:
        n = 8
        c +=1

    elif n == 8:
        n = 7 
        c +=1
    else: 
        break
    print(f'{n} e {c}')