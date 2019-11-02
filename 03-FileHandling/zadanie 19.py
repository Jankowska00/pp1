tab=[]
with open('universities.txt', 'r') as file:
    for i in file:
        tab.append(i)
tab.sort()
with open('universities.txt', 'w') as file:
    for x in tab:
        file.write(x)