import re
allnumbers = 0
with open('land.txt', 'r') as file:
    n = file.read()
    numbers = (re.findall('[0-9]',n))
for i in numbers:
    allnumbers+=int(i)
print(f'Wszystkich cyfr jest {allnumbers}.')
    