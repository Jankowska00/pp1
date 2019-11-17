liczba = 1029
liczba = str(liczba)

def suma(a):
    if len(a) == 1:
        return int(a[0])
    else:
        b = a[0]
        c = []
        for i in range(len(a)):
            if i!=0:
                c.append(a[i])
        return int(b) + suma(c)

print(suma(liczba))