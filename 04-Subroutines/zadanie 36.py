tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]

def suma(tab):
    calkowiteSuma = 0
    for i in tab:
        if type(i) == int:
            calkowiteSuma += i
        elif type(i) == list:
            calkowiteSuma += suma(i)
    return calkowiteSuma

print(suma(tab))