dochod = int(input('Podaj dochód w zł: '))
def podatek(dochod):
    if dochod<=5000:
        print(f'Podatek należny: {0.17*dochod} zł')
    elif dochod>5000:
        print(f'Podatek należny: {5000*0.17+(dochod-5000)*0.32} zł')
podatek(dochod)