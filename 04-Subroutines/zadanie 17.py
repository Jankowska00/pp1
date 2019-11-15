import random
def rzucKostka():
    x = random.randrange(7)
    return x
x = rzucKostka()
y = rzucKostka()
z = rzucKostka()
print(f'Wyrzucone oczka: {x} {y} {z}')
print(f'Suma oczek: {x+y+z}')

    