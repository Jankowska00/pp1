import csv
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    i = 0
    i = str(i)
    for row in reader:
        print(f'{i.ljust(3)}{row[0].ljust(10)}{row[1].ljust(13)} {row[2].ljust(4)} {row[3]}')
        i = int