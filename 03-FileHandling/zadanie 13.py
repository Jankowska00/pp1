with open('liczby.txt', 'a') as file:
    tab = [32, 16, 5, 8, 24, 7]
    for i in range(0, len(tab)):
        tablica = str(tab[i])
        file.write(f'{tablica}\n')