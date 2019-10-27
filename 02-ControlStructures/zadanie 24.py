imiona = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']

najdłuższe_imię=0
x=0
for i in range(0,len(imiona)):
    if len(imiona[i])>x:
        x=len(imiona[i])
        najdłuższe_imię=imiona[i]
print(f'Najdłuższe imię: {najdłuższe_imię}')
    