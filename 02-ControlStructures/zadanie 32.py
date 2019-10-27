x = input('Wprowadź dowolny ciąg znaków: ')

for i in range(1,len(x)+1):
    print(x[-i], end='')