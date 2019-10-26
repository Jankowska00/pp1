N = int(input('Wprowadź N: '))
x = 'Ciąg arytmetyczny o różnicy 3: '
y = -2
while N>0:
    y += 3
    x += str(y)
    N -= 1
    if N>0:
        x += ', '
print(x)
