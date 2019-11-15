def wystepuje(liczba, tablica):
    print(f'Liczba: {liczba}')
    print(f'Tablica:', end=' ')
    for i in range(len(tablica)):
        print(tablica[i], end=' ')
    if liczba in tablica:
        print()
        print('Rezultat: Podana liczba występuje w tablicy')

tablica = [15,38,7,23,14]
liczba = 23
wystepuje(liczba, tablica)