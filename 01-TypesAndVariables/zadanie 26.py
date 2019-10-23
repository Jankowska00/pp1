#Podaj wzrost w cm: ... Podaj wagę w kg: ... Wskaźnik BMI: ... (waga prawidłowa)

# Program obliczający wskaźnik masy ciała BMI (ang. Body Mass Index)

# ustalenie wzrostu i wagi

wzrost=int(input('Podaj wzrost w cm: '))
waga=int(input('Podaj wagę w kg: '))

# przeliczanie wzrost w cm na m

wzrost=wzrost/100

# obliczenie BMI

BMI=(waga/wzrost**2)
print(f'Wskaźnik BMI: {BMI}')

#sprawdzenie czy waga jest prawidłowa

if (BMI >= 18.5 ) and (BMI <= 24.9):
    print('Waga prawidłowa')
else:
    print('Waga nieprawidłowa')