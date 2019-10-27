nazwy = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']

liczba = str(input('Podaj liczbę naturalną: '))

print(f'{liczba} -',end=' ')
for i in range(0, len(liczba)):
    n=int(liczba[i])
    print(nazwy[n],end=' ')