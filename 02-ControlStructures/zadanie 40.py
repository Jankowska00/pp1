import random
kostka = [0,0,0,0,0,0]
for i in range(0,101):
    a=random.randrange(1,7)
    kostka[a-1] += 1
    i += 1
print(f'Szóstka: {kostka[5]}')
print(f'Piątka: {kostka[4]}')
print(f'Czwórka: {kostka[3]}')
print(f'Trójka: {kostka[2]}')
print(f'Dwójka: {kostka[1]}')
print(f'Jedynka: {kostka[0]}')