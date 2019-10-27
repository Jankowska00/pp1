for i in range(3):
    PIN = input('Podaj kod PIN: ')
    if (PIN == '0805'):
        print('Kod PIN poprawny.')
        break
    elif (PIN != '0805') and (i != 2):
        print('Kod PIN niepoprawny.')
    elif (i == 2) and (PIN != '0805'):
        print('Kod PIN niepoprawny.')
        print('Karta płatnicza zostaje zablokowana.')
        