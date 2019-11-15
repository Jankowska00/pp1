def suma(tablica):
         print('Tablica: ',end='')
         for i in range(len(tablica)):
             print(tablica[i],end=' ')
         print()
         print(f'Suma wartości:',sum(tablica))
                 
tablica = [4,3,7,1,3]
suma(tablica)