x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
z = int(input('Podaj trzecią liczbę: '))
tab = [x, y, z]
for i in range(0,2):
    if tab[i+1]<tab[i]:
        (tab[i],tab[i+1])=(tab[i+1],tab[i])
    elif tab[1]<tab[0]:
        (tab[0],tab[1])=(tab[1],tab[0])
print(f'Mediana wynosi {tab[1]}')
