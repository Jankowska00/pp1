def transpozycja(macierz):
    print('Macierz: ')
    print(macierz[0])
    print(macierz[1])
    print(macierz[2])
    print('Macierz transponowana: ')
    print(macierz[0][0], macierz[1][0], macierz[2][0])
    print(macierz[0][1], macierz[1][1], macierz[2][1])
    print(macierz[0][2], macierz[1][2], macierz[2][2])
    
    
macierz = [[1, 2, 0],[0, 0, 3],[5, 1, 1]]
transpozycja(macierz)