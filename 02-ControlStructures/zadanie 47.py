kwota = int(input('Podaj kwotę w zł: '))
monety =[1,2,5]
ilość = [0,0,0]

for i in range(2, -1, -1):
    if (kwota/monety[i]>=1):
        ilość[i]=kwota//monety[i]
        kwota-=ilość[i]*monety[i]
    
print('Kwota 18 zł w monetach: ')
print(f'5 zł - {ilość[2]} szt')
print(f'2 zł - {ilość[1]} szt')
print(f'1 zł - {ilość[0]} szt')