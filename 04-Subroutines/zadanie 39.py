def zakres(x,y,n):
    if n < x or n > y:
        print('Podana liczba nie znajduje się w zakresie <x,y>')
    else:
        print('Podana liczba znajduje się w zakresie <x,y>')
    
    
x = int(input('Podaj dolny zakres: '))
y = int(input('Podaj górny zakres: '))
n = int(input('Podaj liczbę: '))

zakres(x,y,n)
