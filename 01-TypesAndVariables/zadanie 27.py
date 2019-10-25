#program do obliczenia NWD

#ustalanie danych

a = int(input('Wprowadź liczbę naturalną a: '))
b = int(input('Wprowadź liczbę naturalną b: '))

#obliczenie NWD

import math
NWD = math.gcd(a, b)

#warunek na liczby naturalne i podanie wyniku

if a<0 or b<0:
    print('Podane liczby nie spełniają warunku')
else:
    print(f'NWD wynosi: {NWD}')

