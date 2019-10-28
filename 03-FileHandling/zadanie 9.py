with open('NoEducation.txt', 'r') as file:
    x=1
    for line in file:
        print(x, line, end='')
        x+=1