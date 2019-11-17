imiona = ['Janek', 'Ania', 'Wojtek', 'Zosia']
imie = str(input('Podaj imię: '))
def jestImie(imie,imiona):
    print('Imiona: ', end='')
    for i in range(len(imiona)):
        print(imiona[i], end=" ")
    print()
    print(f'Imie: {imie}') 
    if imie in imiona:
        print('Rezultat: imię zawarte jest w wykazie imion')
    else:
        print('Rezultat: imię nie jest zawarte w wykazie imion')

jestImie(imie,imiona)