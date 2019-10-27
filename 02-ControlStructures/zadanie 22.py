tab = [15, 8, 31, 47, 2, 19]
suma = 0
ilość = 0
for i in range(len(tab)):
    if (tab[i]%2 != 0):
        suma += tab[i]
        ilość += 1
        
print(f'Średnia arytmetyczna liczb nieparzystych wynosi: {suma/ilość}')