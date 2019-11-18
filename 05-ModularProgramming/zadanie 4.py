import math
x = 3.7
y = 4
sqrtX = math.sqrt(x)
print(f'Pierwiastek kwadratowy z {x} wynosi {sqrtX}')

power = math.pow(x,y)
print(f'{x} do potęgi {y} wynosi {power}')

sqrtYX = math.pow(x,1/y)
print(f'Pierwiastek {y}-tego stopnia z {x} wynosi {sqrtYX}')

pole = math.pi*y**2
print(f'Pole koła o promieniu {y} wynosi {pole}')

silnia = math.factorial(y)
print(f'Silnia {y} wynosi {silnia}')

najwiekszaCalkowita = math.floor(x)
print(f'Największa liczba całkowita, mniejsza lub równa {x} to {najwiekszaCalkowita}')