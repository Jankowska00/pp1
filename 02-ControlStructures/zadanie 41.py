liczby = []
i = 0
suma = 0
while (liczby != -1):
    liczby.append(int(input('Podaj liczbę: ')))
    suma+=liczby[i]
    if (liczby[i] == 0):
        break
    i += 1
print(f'REZULTAT: Liczb = {len(liczby)-1}, Suma = {suma}, Średnia = {suma/(len(liczby)-1)}')
    
    