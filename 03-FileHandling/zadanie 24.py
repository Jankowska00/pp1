tab=[['Imie','Nazwisko','E-mail'],['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'
],['Piotr','Wyga','wygap@gop.pl']]

with open('csv.csv','w') as file:
    for x in tab:
        for i in x:
            if i!=x[-1]:
                file.write(f'{i},')
            else:
                file.write(f'{i}\n')