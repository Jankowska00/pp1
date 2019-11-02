with open('shoppinglist.txt', 'a') as shopping:
    shopping.write(str(input('Podaj produkt: ')))
    shopping.write('\n')