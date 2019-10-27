n = int(input('Podaj ilość szukanych liczb pierwszych: '))
liczby_pierwsze=[]
i=3
print(f'Liczby pierwsze: ',end=' ')
if n<1:
    print('Error')
else:
    liczby_pierwsze.append(2)
    while len(liczby_pierwsze)<n:
        for d in range(2,i):
                if i%d==0:
                    break
                if d==i-1:
                    liczby_pierwsze.append(i)
        i+=1
    for a in liczby_pierwsze:
        print(a,end=' ')