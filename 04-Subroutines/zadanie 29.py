tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
def mediana(tab):
    tab.sort()
    if len(tab)%2==0:
        srodkowa_1 = int(len(tab)/2)
        srodkowa_2 = int((len(tab)/2)-1)
        x = (tab[srodkowa_1]+tab[srodkowa_2])/2
        print(f'Mediana wynosi: {x}')
    else:
        srodkowa = int((len(tab)/2)-0.5)
        y = tab[srodkowa]
        print(f'Mediana wynosi: {y}')
import statistics
def dominanta(tab):
    print("Dominanta: ",statistics.mode(tab))

mediana(tab)
dominanta(tab)