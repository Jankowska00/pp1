x = float(input('Wprowadź współrzędną x: '))
y = float(input('Wprowadź współrzędną y: '))

if (x>0) and (y>0):
    print(f'Punkt P({x}, {y}) znajduje się w pierwszej ćwiartce układu współrzędnych.')
elif (x<0) and (y>0):
    print(f'Punkt P({x}, {y}) znajduje się w drugiej ćwiartce układu współrzędnych.')
elif (x<0) and (y<0):
    print(f'Punkt P({x}, {y}) znajduje się w trzeciej ćwiartce układu współrzędnych.')
elif (x>0) and (y<0):
    print(f'Punkt P({x}, {y}) znajduje się w czwartej ćwiartce układu współrzędnych.')
elif (x==0) and (y !=0):
    print(f'Punkt P({x}, {y}) leży na osi rzędnych.')
elif (x!=0) and (y==0):
    print(f'Punkt P({x}, {y}) leży na osi odciętych.')
else:
    print(f'Punkt P({x}, {y}) znajduje się w początku osi układu współrzędnych.')