tab = []
with open('numbers.txt', 'r') as file:
    for x in file:
        tab.append(int(x))
tab.sort()
for i in tab:
    print(i, end=' ')