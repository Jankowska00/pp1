a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))


import cmath

delta = b**2-(4*a*c)
if delta > 0:
    p_z_delty = cmath.sqrt(delta)
    pierwiastek1 = ((-b)+(p_z_delty))/2*a
    pierwiastek2 = ((-b)-(p_z_delty))/2*a
    print(f'Pierwiastek = {pierwiastek1} v {pierwiastek2}')
elif delta ==0:
    pierwiastek1 = (-b)/2*a
    print(f'Pierwiastek = {pierwiastek1}')
if delta < 0:
     print(f'Funkcja nie ma pierwiastków.')