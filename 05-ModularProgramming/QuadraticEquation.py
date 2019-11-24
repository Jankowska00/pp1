# odczytaj współczynniki z klawiatury, zwraca tablicę współczynników
def czytajWspolczynniki():
    a = int(input('Wprowadź współczynnik a: '))
    b = int(input('Wprowadź współczynnik b: '))
    c = int(input('Wprowadź współczynnik c: '))
    print(f'Równanie kwadratowe postaci: {a}x2+1{b}x+{c}=0')
    return [a,b,c]
    
# oblicz deltę
def obliczDelte(wspolczynniki):
    return (wspolczynniki[1]^2-4*wspolczynniki[0]*wspolczynniki[2])

# wyznacz pierwiastki równania -zwraca tablicę pierwiastków (jeden lub dwa elementy) lub pustą tablicę, jeśli delta < 0
def obliczPierwiastki(wspolczynniki):
    from math import sqrt
    delta = obliczDelte(wspolczynniki)
    if (delta > 0):
        x1 = (-wspolczynniki[1]-sqrt(delta))/2*wspolczynniki[0]
        x2 = (-wspolczynniki[1]+sqrt(delta))/2*wspolczynniki[0]
        pierwiastki = [x1,x2]
        return pierwiastki
    elif (delta == 0):
        x = (-wspolczynniki[1]+sqrt(delta))/2*wspolczynniki[0]
        pierwiastki = x
        return pierwiastki
    else:
        pierwiastki = []
        return pierwiastki
# wyświetl wyznaczone pierwiastki równania kwadratowego
def wyswietlPierwiastki(pierwiastki):
    print(f'Pierwiastki równania: {pierwiastki}')