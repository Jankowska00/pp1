suma = 0
with open('C:/Users/Wercia_2/Desktop/pp1/03-FileHandling/numbers.txt','r') as numbers:
    for line in numbers:
        suma += int(line)
print(suma)
    