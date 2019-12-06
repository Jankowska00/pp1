import random

class cube():
    
    def __init__(self):
        self.number = 0 # kostka przed rzutem
    
    def throw(self):
        self.number = random.randint(1,6)
        
    def show(self):
        print(self.number)
        
    def nr(self):
        return self.number

for i in range(5):             
    x1 = cube()
    x2 = cube()
    x3 = cube()

    x1.throw()
    x2.throw()
    x3.throw()

    x1.show()
    x2.show()
    x3.show()

    suma = x1.nr() + x2.nr() + x3.nr()
    print(f'Suma wynosi: {suma}\n')


    
            
    
    



    