import re
ilosc=0
suma=0
with open('numbersinrows.txt','r') as numbers:
    for x in numbers:
        tab = re.split(',',x)
        ilosc+=len(tab)
        for i in tab:
            suma+=int(i)
print(f'Ilość liczb:{ilosc}\nSuma:{suma}')