
print('Obliczanie pola powierzchni i obwodu koła o zadanym promieniu')
print('')
import cmath
PI = cmath.pi
r = int(input('Wprowadź promień koła r: '))

pole = (PI*r**2)
obwód = (2*PI*r)

print(f'Pole koła o promieniu {r} wynosi {pole}')
print(f'Obwód koła o promieniu {r} wynosi {obwód}')