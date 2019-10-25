# program do obliczenia sumy i wyniku losowania trzy razy kostką

import random

# rzucanie trzy razy kostką


x = random.randint(1,6)
y = random.randint(1,6)
z = random.randint(1,6)

# wyświetlenie wyniku trzech losowań

print(f'Wylosowane liczby to: {x}, {y}, {z}')

# obliczenie sumy wyrzuconych oczek

suma = x+y+z

print(f'Suma wyrzuconych oczek wynosi: {suma}')

