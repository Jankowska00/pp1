x = int(input('Podaj limit prędkości (km/h): '))
y = int(input('Podaj prędkość pojazdu (km/h): '))

if y<x:
    mandat = 0
elif (y-x)<=10:
    mandat = (y-x)*5
else:
    mandat = 50+(y-10-x)*15
    
print(f' Mandat (zł): {mandat}')