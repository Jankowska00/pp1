with open('numbers.txt', 'r') as numbers:
    for x in numbers:
        if (int(x)>0) and (int(x)%2==0):
            with open('evennumbers.txt', 'a') as evennumbers:
                evennumbers.write(x)
        
        
    
    