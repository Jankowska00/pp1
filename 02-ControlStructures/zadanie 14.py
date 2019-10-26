x = int(input('Podaj wiek psa w ludzkich latach: '))

if (x<=2):
    print(f'Wiek psa w psich latach to {x*10.5}')
else:
    print(f'Wiek psa w psich latach to {21+(x-2)*4}')