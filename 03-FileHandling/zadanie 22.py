import re
with open('students.txt', 'r') as students:
    for line in students:
        data = re.split(',',line)
        if data[2] != 'age':
            if int(data[2])<30:
                print('{}  {}  {}'.format(data[0] ,data[1],data[4] ))
                