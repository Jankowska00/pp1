pesel = str(input('Podaj Pesel: '))

if int(pesel[-2])%2 == 0 :
    plec = 'kobieta'
else:
    plec = 'mężczyzna'
    
print(plec)

if int(pesel[2])>1:
    rok = 2000+int(pesel[0:2])
else:
    rok = 1900+int(pesel[0:2])
wiek = 2019 - rok

print(wiek)