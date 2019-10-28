# wariant 1
#file =open('NoEducation.txt', 'r')
#print( file.read() )
#file.close()

#wariant 2
with open('NoEducation.txt', 'r') as file:
    print( file.read() )
