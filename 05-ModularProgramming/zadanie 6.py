import csv
import statistics
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    i = 1
    x = '#'
    tab = []
    row1 = next(reader)
    print(f'{x.ljust(5)}{row1[0].ljust(10).upper()}{row1[1].ljust(15).upper()}{row1[2].ljust(6).upper()}{row1[3].upper()}')
    print("==========================================================================")
    for row in reader:
        i = str(i)
        i.replace('0','#')
        print(f'{i.ljust(5)}{row[0].ljust(10).upper()}{row[1].ljust(15)}{row[2].ljust(6)}{row[3]}')
        i = int(i)
        i += 1
        tab.append(row[2])
    tab = [int(x) for x in tab]
    srednia = statistics.mean(tab)
    print()
    print(f'Średnia wieku pracowników to: {srednia}')
    
    